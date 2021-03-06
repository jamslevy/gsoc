#!/usr/bin/python2.5
#
# Copyright 2009 the Melange authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Starts an interactive shell with statistic helpers.
"""

__authors__ = [
  '"Sverre Rabbelier" <sverre@rabbelier.nl>',
]


import cPickle
import datetime
import operator
import sys
import time

import interactive


def dateFetch(queryGen, last=None, batchSize=100):
  """Iterator that yields an entity in batches.

  Args:
    queryGen: should return a Query object
    last: used to .filter() for last_modified_on
    batchSize: how many entities to retrieve in one datastore call

  Retrieved from http://tinyurl.com/d887ll (AppEngine cookbook).
  """

  from google.appengine.ext import db

   # AppEngine will not fetch more than 1000 results
  batchSize = min(batchSize,1000)

  query = None
  done = False
  count = 0

  while not done:
    print count
    query = queryGen()
    query.order('last_modified_on')
    if last:
      query.filter("last_modified_on > ", last)
    results = query.fetch(batchSize)
    for result in results:
      count += 1
      yield result
    if batchSize > len(results):
      done = True
    else:
      last = results[-1].last_modified_on


def addKey(target, fieldname):
  """Adds the key of the specified field.
  """

  result = target.copy()
  result['%s_key' % fieldname] = target[fieldname].key().name()
  return result


def getEntities(model):
  """Returns all users as dictionary.
  """

  def wrapped():
    gen = lambda: model.all()
    it = interactive.deepFetch(gen)

    entities = [(i.key().name(), i) for i in it]
    return dict(entities)

  return wrapped


def getProps(last=None):
  """Returns all proposals as a list of dictionaries.
  """

  key_order = [
      'link_id', 'scope_path', 'title', 'abstract', 'content',
      'additional_info', '_mentor', 'possible_mentors', 'score',
      'status', '_org', 'created_on', 'last_modified_on']

  from soc.models.student_proposal import StudentProposal

  gen = lambda: StudentProposal.all()

  it = dateFetch(gen, last)

  proposals = [(i.key().name(), i.toDict(key_order)) for i in it]
  if proposals:
    last = i.last_modified_on # last modified entity
  else:
    last = datetime.datetime.now()

  return dict(proposals), last


def orgStats(target, orgs):
  """Retrieves org stats.
  """

  from soc.logic import dicts

  orgs = [(v.key(), v) for k, v in orgs.iteritems()]
  orgs = dict(orgs)

  grouped = dicts.groupby(target.values(), '_org')

  grouped = [(orgs[k], v) for k, v in grouped.iteritems()]
  popularity = [(k.link_id, len(v)) for k, v in grouped]

  return dict(grouped), dict(popularity)


def countStudentsWithProposals():
  """Retrieves number of Students who have submitted at least one Student Proposal.
  """

  proposals = getStudentProposals()
  students = {}

  for proposal_key in proposals.keys():
    students[proposals[proposal_key].scope_path] = True

  return len(students)


def printPopularity(popularity):
  """Prints the popularity for the specified proposals.
  """

  g = operator.itemgetter(1)

  for item in sorted(popularity.iteritems(), key=g, reverse=True):
    print "%s: %d" % item


def saveValues(values, saver):
  """Saves the specified popularities.
  """

  import logging
  from google.appengine.ext import db

  from soc.models.organization import Organization

  def txn(key, value):
    org = Organization.get_by_key_name(key)
    saver(org, value)
    org.put()

  for key, value in sorted(values.iteritems()):
    print key
    db.run_in_transaction_custom_retries(10, txn, key, value)

  print "done"


def addFollower(follower, proposals, add_public=True, add_private=True):
  """Adds a user as follower to the specified proposals.

  Args:
    follower: the User to add as follower
    proposals: a list with the StudnetProposals that should be subscribed to
    add_public: whether the user is subscribed to public updates
    add_private: whether the user should be subscribed to private updates
  """

  from soc.models.review_follower import ReviewFollower

  result = []

  for i in proposals:
     properties = {
       'user': follower,
       'link_id': follower.link_id,
       'scope': i,
       'scope_path': i.key().name(),
       'key_name': '%s/%s' % (i.key().name(), follower.link_id),
       'subscribed_public': add_public,
       'subscribed_private': add_private,
     }

     entity = ReviewFollower(**properties)
     result.append(entity)

  return result


def convertProposals(org):
  """Convert all proposals for the specified organization.

  Args:
    org: the organization for which all proposals will be converted
  """

  from soc.logic.models.student_proposal import logic as proposal_logic
  from soc.logic.models.student_project import logic as project_logic

  proposals = proposal_logic.getProposalsToBeAcceptedForOrg(org)

  print "accepting %d proposals, with %d slots" % (len(proposals), org.slots)

  for proposal in proposals:
    fields = {
        'link_id': 't%i' % (int(time.time()*100)),
        'scope_path': proposal.org.key().id_or_name(),
        'scope': proposal.org,
        'program': proposal.program,
        'student': proposal.scope,
        'title': proposal.title,
        'abstract': proposal.abstract,
        'mentor': proposal.mentor,
        }

    project = project_logic.updateOrCreateFromFields(fields, silent=True)

    fields = {
        'status':'accepted',
        }

    proposal_logic.updateEntityProperties(proposal, fields, silent=True)

  fields = {
      'status': ['new', 'pending'],
      'org': org,
      }

  querygen = lambda: proposal_logic.getQueryForFields(fields)
  proposals = [i for i in interactive.deepFetch(querygen, batchSize=10)]

  print "rejecting %d proposals" % len(proposals)

  fields = {
      'status': 'rejected',
      }

  for proposal in proposals:
    proposal_logic.updateEntityProperties(proposal, fields, silent=True)


def startSpam():
  """Creates the job that is responsible for sending mails.
  """

  from soc.logic.models.job import logic as job_logic
  from soc.logic.models.priority_group import logic as priority_logic
  from soc.logic.models.program import logic as program_logic

  program_entity = program_logic.getFromKeyName('google/gsoc2009')

  priority_group = priority_logic.getGroup(priority_logic.EMAIL)
  job_fields = {
      'priority_group': priority_group,
      'task_name': 'setupStudentProposalMailing',
      'key_data': [program_entity.key()]}

  job_logic.updateOrCreateFromFields(job_fields)


def reviveJobs(amount):
  """Sets jobs that are stuck in 'aborted' to waiting.

  Args:
    amount: the amount of jobs to revive
  """

  from soc.models.job import Job

  query = Job.all().filter('status', 'aborted')
  jobs = query.fetch(amount)

  if not jobs:
    print "no dead jobs"

  for job in jobs:
     job.status = 'waiting'
     job.put()
     print "restarted %d" % job.key().id()


def deidleJobs(amount):
  """Sets jobs that are stuck in 'started' to waiting.

  Args:
    amount: the amount of jobs to deidle
  """

  from soc.models.job import Job

  query = Job.all().filter('status', 'started')
  jobs = query.fetch(amount)

  if not jobs:
    print "no idle jobs"

  for job in jobs:
     job.status = 'waiting'
     job.put()
     print "restarted %d" % job.key().id()


def deleteEntities(model, step_size=25):
  """Deletes all entities of the specified type
  """

  print "Deleting..."
  count = 0

  while True:
    entities = model.all().fetch(step_size)

    if not entities:
      break

    for entity in entities:
      entity.delete()

    count += step_size

    print "deleted %d entities" % count

  print "Done"

def loadPickle(name):
  """Loads a pickle.
  """

  f = open(name + '.dat')
  return cPickle.load(f)


def dumpPickle(target, name):
  """Dumps a pickle.
  """

  f = open("%s.dat" % name, 'w')
  cPickle.dump(target, f)


def main(args):
  """Main routine.
  """

  interactive.setup()

  from soc.models.organization import Organization
  from soc.models.user import User
  from soc.models.student import Student
  from soc.models.mentor import Mentor
  from soc.models.org_admin import OrgAdmin
  from soc.models.job import Job
  from soc.models.student_proposal import StudentProposal
  from soc.models.student_project import StudentProject

  def slotSaver(org, value):
    org.slots = value
  def popSaver(org, value):
    org.nr_applications = value
  def rawSaver(org, value):
    org.slots_calculated = value

  context = {
      'load': loadPickle,
      'dump': dumpPickle,
      'orgStats': orgStats,
      'printPopularity': printPopularity,
      'saveValues': saveValues,
      'getEntities': getEntities,
      'deleteEntities': deleteEntities,
      'getOrgs': getEntities(Organization),
      'getUsers': getEntities(User),
      'getStudents': getEntities(Student),
      'getMentors': getEntities(Mentor),
      'getOrgAdmins': getEntities(OrgAdmin),
      'getStudentProjects': getEntities(StudentProject),
      'getProps': getProps,
      'countStudentsWithProposals': countStudentsWithProposals,
      'convertProposals': convertProposals,
      'addFollower': addFollower,
      'Organization': Organization,
      'Job': Job,
      'User': User,
      'Student': Student,
      'Mentor': Mentor,
      'OrgAdmin': OrgAdmin,
      'StudentProject': StudentProject,
      'StudentProposal': StudentProposal,
      'slotSaver': slotSaver,
      'popSaver': popSaver,
      'rawSaver': rawSaver,
      'startSpam': startSpam,
      'reviveJobs': reviveJobs,
      'deidleJobs': deidleJobs,
  }

  interactive.remote(args, context)

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print "Usage: %s app_id [host]" % (sys.argv[0],)
    sys.exit(1)

  main(sys.argv[1:])
