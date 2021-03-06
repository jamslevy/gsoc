#!/usr/bin/python2.5
#
# Copyright 2008 the Melange authors.
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

"""Views for User profiles.
"""

__authors__ = [
    '"Sverre Rabbelier" <sverre@rabbelier.nl>',
    '"Lennard de Rijk" <ljvderijk@gmail.com>',
    '"Pawel Solyga" <pawel.solyga@gmail.com>',
  ]


from django import forms

from soc.logic import cleaning
from soc.logic import dicts
from soc.logic.models.site import logic as site_logic
from soc.logic.models.user import logic as user_logic
from soc.views.helper import access
from soc.views.helper import decorators
from soc.views.helper import redirects
from soc.views.helper import widgets
from soc.views.models import base

import soc.models.linkable
import soc.logic.models.user
import soc.views.helper


class View(base.View):
  """View methods for the User model.
  """


  def __init__(self, params=None):
    """Defines the fields and methods required for the base View class
    to provide the user with list, public, create, edit and delete views.

    Params:
      params: a dict with params for this View
    """

    rights = access.Checker(params)
    rights['create'] = ['checkIsDeveloper']
    rights['edit'] = ['checkIsDeveloper']
    rights['delete'] = ['checkIsDeveloper']
    rights['show'] = ['allow']
    rights['list'] = ['checkIsDeveloper']
    rights['list_developers'] = ['checkIsDeveloper']

    new_params = {}
    new_params['logic'] = soc.logic.models.user.logic
    new_params['rights'] = rights
    
    new_params['name'] = "User"

    new_params['edit_template'] = 'soc/user/edit.html'
    new_params['pickable'] = True
    new_params['cache_pick'] = True

    new_params['sidebar_heading'] = 'Users'

    new_params['extra_dynaexclude'] = ['former_accounts', 'agreed_to_tos',
        'agreed_to_tos_on', 'status']
    new_params['create_extra_dynaproperties'] = {
        'clean_link_id': cleaning.clean_user_not_exist('link_id'),
        'clean_account': cleaning.clean_user_account_not_in_use('account')}

    # recreate the choices for the edit form
    status_choices = []
    for choice in user_logic.getModel().status.choices:
      status_choices.append((choice, choice))

    new_params['edit_extra_dynaproperties'] = {
        'link_id': forms.CharField(widget=widgets.ReadOnlyInput(),
            required=True),
        'clean_link_id': cleaning.clean_link_id('link_id'),
        'agreed_to_tos_on': forms.DateTimeField(
            widget=widgets.ReadOnlyInput(attrs={'disabled':'true'}),
            required=False),
        'status': forms.ChoiceField(choices=status_choices),
        'clean_account': cleaning.clean_user_account('account'),
        'clean': cleaning.validate_user_edit('link_id', 'account'),
    }

    patterns = []

    patterns += [(r'^%(url_name)s/(?P<access_type>list_developers)$',
                  'soc.views.models.%(module_name)s.list_developers', 
                  "List Developers")]

    new_params['extra_django_patterns'] = patterns

    new_params['sidebar_additional'] = [
        ('/user/list_developers' % new_params,
         'List Developers', 'list_developers'),]

    params = dicts.merge(params, new_params)

    super(View, self).__init__(params=params)

  def listDevelopers(self, request, access_type, page_name=None, params=None):
    """See base.View.list.
    """

    filter = {'is_developer': True}

    return self.list(request, access_type, page_name=page_name,
                     params=params, filter=filter)

  def _editGet(self, request, entity, form):
    """See base.View._editGet().
    """

    # fill in the email field with the data from the entity
    form.fields['account'].initial = entity.account.email
    form.fields['agreed_to_tos_on'].initial = entity.agreed_to_tos_on
    form.fields['agreed_to_tos_on'].example_text = self._getToSExampleText()
    form.fields['status'].initial = entity.status

    super(View, self)._editGet(request, entity, form)


  def _getToSExampleText(self):
    """Returns example_text linking to site-wide ToS, or a warning message.
    """
    tos_link = redirects.getToSRedirect(site_logic.getSingleton())

    if not tos_link:
      return ('<div class="notice">&nbsp;<i>No site-wide</i> Terms of'
              ' Service <i>are currently set!</i>&nbsp;</div>')

    return ('<i>current site-wide <b><a href=%s>Terms of Service</a></b></i>'
            % tos_link)


view = View()

admin = decorators.view(view.admin)
create = decorators.view(view.create)
delete = decorators.view(view.delete)
edit = decorators.view(view.edit)
list = decorators.view(view.list)
list_developers = decorators.view(view.listDevelopers)
public = decorators.view(view.public)
export = decorators.view(view.export)
pick = decorators.view(view.pick)
