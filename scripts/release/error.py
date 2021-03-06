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

__authors__ = [
    # alphabetical order by last name, please
    '"David Anderson" <dave@natulte.net>',
    ]


class Error(Exception):
  """Base class for release script exceptions."""
  pass


class ObstructionError(Error):
  """An operation was obstructed by existing data."""
  pass


class ExpectationFailed(Error):
  """An unexpected state was encountered by an automated step."""
  pass


class AbortedByUser(Error):
  """The operation was aborted by the user."""
  pass
