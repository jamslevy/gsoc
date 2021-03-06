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

"""This module contains the Group Application Model."""

__authors__ = [
  '"Todd Larsen" <tlarsen@google.com>',
]


from google.appengine.ext import db

from django.utils.translation import ugettext

import soc.models.document
import soc.models.linkable
import soc.models.user


class GroupApplication(soc.models.linkable.Linkable):
  """Common application questions for all groups.

  Eventually, this will be replaced with a Question/Answer/Quiz/Response
  approach.  At that time, existing OrgApplication entities will be migrated
  (converted) to their new representations in the Datastore.
  """

  #: Required field that will become the name of the Group in the profile,
  #: if the Group Application is accepted.
  #: See also:  soc.models.group.Group.name
  name = db.StringProperty(required=True,
      verbose_name=ugettext('Group Name'))
  name.help_text = ugettext('Complete, formal name of the group.')  
  
  #: Required many:1 relationship indicating the User who is applying on
  #: behalf of the Group.  If the Group Application is accepted, this User
  #: will become the founding User of the Group.
  #: See also:  soc.models.group.Group.founder
  applicant = db.ReferenceProperty(reference_class=soc.models.user.User,
    required=True, collection_name='group_apps',
    verbose_name=ugettext('Applicant'))

  #: Required field indicating the home page URL of the applying Group.
  #: See also:  soc.models.group.Group.home_page
  home_page = db.LinkProperty(required=True,
      verbose_name=ugettext('Home Page URL'))
  
  #: Required email address used as the "public" contact mechanism for
  #: the Group (as opposed to the applicant.account email address which is
  #: kept secret, revealed only to Developers).
  #: See also:  soc.models.group.Group.email
  email = db.EmailProperty(required=True,
    verbose_name=ugettext('Public Email'))
  email.help_text = ugettext(
      "Enter an email address to be used by would-be members seeking "
      "additional information. This can be an individual's email address or a "
      "mailing list address; use whichever will work best for you.")

  #: Required description of the Group.
  description = db.TextProperty(required=True,
      verbose_name=ugettext('Description'))

  why_applying = db.TextProperty(required=True,
    verbose_name=ugettext(
      'Why is your group applying to participate?'
      ' What do you hope to gain by participating?'))

  pub_mailing_list = db.StringProperty(required=True,
    verbose_name=ugettext(
      'What is the main public mailing list for your group?'))
  pub_mailing_list.help_text = ugettext(
    'Mailing list email address, URL to sign-up page, etc. If a mailing '
    'list is not used please specify another method of communication used '
    'within the group.')

  irc_channel = db.StringProperty(required=True,
    verbose_name=ugettext(
      'Where is the main IRC channel for your group?'))
  irc_channel.help_text = ugettext('IRC network and channel. If IRC is '
      'not used please write something like not applicable.')

  backup_admin = db.ReferenceProperty(reference_class=soc.models.user.User,
    required=False, collection_name='group_app_backup_admin',
    verbose_name=ugettext(
      'Please select your backup group administrator.'))

  member_criteria = db.TextProperty(required=True,
    verbose_name=ugettext(
      'What criteria do you use to select the members of your group?'
      ' Please be as specific as possible.'))
  member_criteria.help_text = ugettext(
    'Members include mentors, administrators, and the like.')

  # property containing the status of the application
  # completed means that the application has been processed into a real group
  # pre-accepted: used to indicate that the application has been accepted
  # but the group cannot be made yet.
  # pre-rejected: used to indicate that the application has been rejected
  # but the applicant has not been informed yet.
  status = db.StringProperty(required=True,
      choices=['accepted','rejected','ignored','needs review','completed',
          'pre-accepted', 'pre-rejected'],
      default='needs review',
      verbose_name=ugettext('Application Status'))

  # timestamp to record the time on which this application has been created
  created_on = db.DateTimeProperty(required=True, auto_now_add=True,
      verbose_name=ugettext('Created on'))
  
  # timestamp to record the time on which this application has been 
  # last modified also changes when the review properties change
  last_modified_on = db.DateTimeProperty(required=True, auto_now=True,
      verbose_name=ugettext('Last modified on'))
