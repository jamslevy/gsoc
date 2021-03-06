#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.net.proto import ProtocolBuffer
import array
import dummy_thread as thread

__pychecker__ = """maxreturns=0 maxbranches=0 no-callinit
                   unusednames=printElemNumber,debug_strs no-special"""

from google.appengine.api.api_base_pb import VoidProto
class MemcacheServiceError(ProtocolBuffer.ProtocolMessage):

  OK           =    0
  UNSPECIFIED_ERROR =    1

  _ErrorCode_NAMES = {
    0: "OK",
    1: "UNSPECIFIED_ERROR",
  }

  def ErrorCode_Name(cls, x): return cls._ErrorCode_NAMES.get(x, "")
  ErrorCode_Name = classmethod(ErrorCode_Name)


  def __init__(self, contents=None):
    pass
    if contents is not None: self.MergeFromString(contents)


  def MergeFrom(self, x):
    assert x is not self

  def Equals(self, x):
    if x is self: return 1
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    return initialized

  def ByteSize(self):
    n = 0
    return n + 0

  def Clear(self):
    pass

  def OutputUnchecked(self, out):
    pass

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    return res


  _TEXT = (
   "ErrorCode",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class MemcacheGetRequest(ProtocolBuffer.ProtocolMessage):
  has_name_space_ = 0
  name_space_ = ""

  def __init__(self, contents=None):
    self.key_ = []
    if contents is not None: self.MergeFromString(contents)

  def key_size(self): return len(self.key_)
  def key_list(self): return self.key_

  def key(self, i):
    return self.key_[i]

  def set_key(self, i, x):
    self.key_[i] = x

  def add_key(self, x):
    self.key_.append(x)

  def clear_key(self):
    self.key_ = []

  def name_space(self): return self.name_space_

  def set_name_space(self, x):
    self.has_name_space_ = 1
    self.name_space_ = x

  def clear_name_space(self):
    if self.has_name_space_:
      self.has_name_space_ = 0
      self.name_space_ = ""

  def has_name_space(self): return self.has_name_space_


  def MergeFrom(self, x):
    assert x is not self
    for i in xrange(x.key_size()): self.add_key(x.key(i))
    if (x.has_name_space()): self.set_name_space(x.name_space())

  def Equals(self, x):
    if x is self: return 1
    if len(self.key_) != len(x.key_): return 0
    for e1, e2 in zip(self.key_, x.key_):
      if e1 != e2: return 0
    if self.has_name_space_ != x.has_name_space_: return 0
    if self.has_name_space_ and self.name_space_ != x.name_space_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    return initialized

  def ByteSize(self):
    n = 0
    n += 1 * len(self.key_)
    for i in xrange(len(self.key_)): n += self.lengthString(len(self.key_[i]))
    if (self.has_name_space_): n += 1 + self.lengthString(len(self.name_space_))
    return n + 0

  def Clear(self):
    self.clear_key()
    self.clear_name_space()

  def OutputUnchecked(self, out):
    for i in xrange(len(self.key_)):
      out.putVarInt32(10)
      out.putPrefixedString(self.key_[i])
    if (self.has_name_space_):
      out.putVarInt32(18)
      out.putPrefixedString(self.name_space_)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 10:
        self.add_key(d.getPrefixedString())
        continue
      if tt == 18:
        self.set_name_space(d.getPrefixedString())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    cnt=0
    for e in self.key_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("key%s: %s\n" % (elm, self.DebugFormatString(e)))
      cnt+=1
    if self.has_name_space_: res+=prefix+("name_space: %s\n" % self.DebugFormatString(self.name_space_))
    return res

  kkey = 1
  kname_space = 2

  _TEXT = (
   "ErrorCode",
   "key",
   "name_space",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STRING,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class MemcacheGetResponse_Item(ProtocolBuffer.ProtocolMessage):
  has_key_ = 0
  key_ = ""
  has_value_ = 0
  value_ = ""
  has_flags_ = 0
  flags_ = 0

  def __init__(self, contents=None):
    if contents is not None: self.MergeFromString(contents)

  def key(self): return self.key_

  def set_key(self, x):
    self.has_key_ = 1
    self.key_ = x

  def clear_key(self):
    if self.has_key_:
      self.has_key_ = 0
      self.key_ = ""

  def has_key(self): return self.has_key_

  def value(self): return self.value_

  def set_value(self, x):
    self.has_value_ = 1
    self.value_ = x

  def clear_value(self):
    if self.has_value_:
      self.has_value_ = 0
      self.value_ = ""

  def has_value(self): return self.has_value_

  def flags(self): return self.flags_

  def set_flags(self, x):
    self.has_flags_ = 1
    self.flags_ = x

  def clear_flags(self):
    if self.has_flags_:
      self.has_flags_ = 0
      self.flags_ = 0

  def has_flags(self): return self.has_flags_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_key()): self.set_key(x.key())
    if (x.has_value()): self.set_value(x.value())
    if (x.has_flags()): self.set_flags(x.flags())

  def Equals(self, x):
    if x is self: return 1
    if self.has_key_ != x.has_key_: return 0
    if self.has_key_ and self.key_ != x.key_: return 0
    if self.has_value_ != x.has_value_: return 0
    if self.has_value_ and self.value_ != x.value_: return 0
    if self.has_flags_ != x.has_flags_: return 0
    if self.has_flags_ and self.flags_ != x.flags_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_key_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: key not set.')
    if (not self.has_value_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: value not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(len(self.key_))
    n += self.lengthString(len(self.value_))
    if (self.has_flags_): n += 5
    return n + 2

  def Clear(self):
    self.clear_key()
    self.clear_value()
    self.clear_flags()

  def OutputUnchecked(self, out):
    out.putVarInt32(18)
    out.putPrefixedString(self.key_)
    out.putVarInt32(26)
    out.putPrefixedString(self.value_)
    if (self.has_flags_):
      out.putVarInt32(37)
      out.put32(self.flags_)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 12: break
      if tt == 18:
        self.set_key(d.getPrefixedString())
        continue
      if tt == 26:
        self.set_value(d.getPrefixedString())
        continue
      if tt == 37:
        self.set_flags(d.get32())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_key_: res+=prefix+("key: %s\n" % self.DebugFormatString(self.key_))
    if self.has_value_: res+=prefix+("value: %s\n" % self.DebugFormatString(self.value_))
    if self.has_flags_: res+=prefix+("flags: %s\n" % self.DebugFormatFixed32(self.flags_))
    return res

class MemcacheGetResponse(ProtocolBuffer.ProtocolMessage):

  def __init__(self, contents=None):
    self.item_ = []
    if contents is not None: self.MergeFromString(contents)

  def item_size(self): return len(self.item_)
  def item_list(self): return self.item_

  def item(self, i):
    return self.item_[i]

  def mutable_item(self, i):
    return self.item_[i]

  def add_item(self):
    x = MemcacheGetResponse_Item()
    self.item_.append(x)
    return x

  def clear_item(self):
    self.item_ = []

  def MergeFrom(self, x):
    assert x is not self
    for i in xrange(x.item_size()): self.add_item().CopyFrom(x.item(i))

  def Equals(self, x):
    if x is self: return 1
    if len(self.item_) != len(x.item_): return 0
    for e1, e2 in zip(self.item_, x.item_):
      if e1 != e2: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    for p in self.item_:
      if not p.IsInitialized(debug_strs): initialized=0
    return initialized

  def ByteSize(self):
    n = 0
    n += 2 * len(self.item_)
    for i in xrange(len(self.item_)): n += self.item_[i].ByteSize()
    return n + 0

  def Clear(self):
    self.clear_item()

  def OutputUnchecked(self, out):
    for i in xrange(len(self.item_)):
      out.putVarInt32(11)
      self.item_[i].OutputUnchecked(out)
      out.putVarInt32(12)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 11:
        self.add_item().TryMerge(d)
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    cnt=0
    for e in self.item_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("Item%s {\n" % elm)
      res+=e.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
      cnt+=1
    return res

  kItemGroup = 1
  kItemkey = 2
  kItemvalue = 3
  kItemflags = 4

  _TEXT = (
   "ErrorCode",
   "Item",
   "key",
   "value",
   "flags",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.STARTGROUP,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.FLOAT,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class MemcacheSetRequest_Item(ProtocolBuffer.ProtocolMessage):
  has_key_ = 0
  key_ = ""
  has_value_ = 0
  value_ = ""
  has_flags_ = 0
  flags_ = 0
  has_set_policy_ = 0
  set_policy_ = 1
  has_expiration_time_ = 0
  expiration_time_ = 0

  def __init__(self, contents=None):
    if contents is not None: self.MergeFromString(contents)

  def key(self): return self.key_

  def set_key(self, x):
    self.has_key_ = 1
    self.key_ = x

  def clear_key(self):
    if self.has_key_:
      self.has_key_ = 0
      self.key_ = ""

  def has_key(self): return self.has_key_

  def value(self): return self.value_

  def set_value(self, x):
    self.has_value_ = 1
    self.value_ = x

  def clear_value(self):
    if self.has_value_:
      self.has_value_ = 0
      self.value_ = ""

  def has_value(self): return self.has_value_

  def flags(self): return self.flags_

  def set_flags(self, x):
    self.has_flags_ = 1
    self.flags_ = x

  def clear_flags(self):
    if self.has_flags_:
      self.has_flags_ = 0
      self.flags_ = 0

  def has_flags(self): return self.has_flags_

  def set_policy(self): return self.set_policy_

  def set_set_policy(self, x):
    self.has_set_policy_ = 1
    self.set_policy_ = x

  def clear_set_policy(self):
    if self.has_set_policy_:
      self.has_set_policy_ = 0
      self.set_policy_ = 1

  def has_set_policy(self): return self.has_set_policy_

  def expiration_time(self): return self.expiration_time_

  def set_expiration_time(self, x):
    self.has_expiration_time_ = 1
    self.expiration_time_ = x

  def clear_expiration_time(self):
    if self.has_expiration_time_:
      self.has_expiration_time_ = 0
      self.expiration_time_ = 0

  def has_expiration_time(self): return self.has_expiration_time_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_key()): self.set_key(x.key())
    if (x.has_value()): self.set_value(x.value())
    if (x.has_flags()): self.set_flags(x.flags())
    if (x.has_set_policy()): self.set_set_policy(x.set_policy())
    if (x.has_expiration_time()): self.set_expiration_time(x.expiration_time())

  def Equals(self, x):
    if x is self: return 1
    if self.has_key_ != x.has_key_: return 0
    if self.has_key_ and self.key_ != x.key_: return 0
    if self.has_value_ != x.has_value_: return 0
    if self.has_value_ and self.value_ != x.value_: return 0
    if self.has_flags_ != x.has_flags_: return 0
    if self.has_flags_ and self.flags_ != x.flags_: return 0
    if self.has_set_policy_ != x.has_set_policy_: return 0
    if self.has_set_policy_ and self.set_policy_ != x.set_policy_: return 0
    if self.has_expiration_time_ != x.has_expiration_time_: return 0
    if self.has_expiration_time_ and self.expiration_time_ != x.expiration_time_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_key_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: key not set.')
    if (not self.has_value_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: value not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(len(self.key_))
    n += self.lengthString(len(self.value_))
    if (self.has_flags_): n += 5
    if (self.has_set_policy_): n += 1 + self.lengthVarInt64(self.set_policy_)
    if (self.has_expiration_time_): n += 5
    return n + 2

  def Clear(self):
    self.clear_key()
    self.clear_value()
    self.clear_flags()
    self.clear_set_policy()
    self.clear_expiration_time()

  def OutputUnchecked(self, out):
    out.putVarInt32(18)
    out.putPrefixedString(self.key_)
    out.putVarInt32(26)
    out.putPrefixedString(self.value_)
    if (self.has_flags_):
      out.putVarInt32(37)
      out.put32(self.flags_)
    if (self.has_set_policy_):
      out.putVarInt32(40)
      out.putVarInt32(self.set_policy_)
    if (self.has_expiration_time_):
      out.putVarInt32(53)
      out.put32(self.expiration_time_)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 12: break
      if tt == 18:
        self.set_key(d.getPrefixedString())
        continue
      if tt == 26:
        self.set_value(d.getPrefixedString())
        continue
      if tt == 37:
        self.set_flags(d.get32())
        continue
      if tt == 40:
        self.set_set_policy(d.getVarInt32())
        continue
      if tt == 53:
        self.set_expiration_time(d.get32())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_key_: res+=prefix+("key: %s\n" % self.DebugFormatString(self.key_))
    if self.has_value_: res+=prefix+("value: %s\n" % self.DebugFormatString(self.value_))
    if self.has_flags_: res+=prefix+("flags: %s\n" % self.DebugFormatFixed32(self.flags_))
    if self.has_set_policy_: res+=prefix+("set_policy: %s\n" % self.DebugFormatInt32(self.set_policy_))
    if self.has_expiration_time_: res+=prefix+("expiration_time: %s\n" % self.DebugFormatFixed32(self.expiration_time_))
    return res

class MemcacheSetRequest(ProtocolBuffer.ProtocolMessage):

  SET          =    1
  ADD          =    2
  REPLACE      =    3

  _SetPolicy_NAMES = {
    1: "SET",
    2: "ADD",
    3: "REPLACE",
  }

  def SetPolicy_Name(cls, x): return cls._SetPolicy_NAMES.get(x, "")
  SetPolicy_Name = classmethod(SetPolicy_Name)

  has_name_space_ = 0
  name_space_ = ""

  def __init__(self, contents=None):
    self.item_ = []
    if contents is not None: self.MergeFromString(contents)

  def item_size(self): return len(self.item_)
  def item_list(self): return self.item_

  def item(self, i):
    return self.item_[i]

  def mutable_item(self, i):
    return self.item_[i]

  def add_item(self):
    x = MemcacheSetRequest_Item()
    self.item_.append(x)
    return x

  def clear_item(self):
    self.item_ = []
  def name_space(self): return self.name_space_

  def set_name_space(self, x):
    self.has_name_space_ = 1
    self.name_space_ = x

  def clear_name_space(self):
    if self.has_name_space_:
      self.has_name_space_ = 0
      self.name_space_ = ""

  def has_name_space(self): return self.has_name_space_


  def MergeFrom(self, x):
    assert x is not self
    for i in xrange(x.item_size()): self.add_item().CopyFrom(x.item(i))
    if (x.has_name_space()): self.set_name_space(x.name_space())

  def Equals(self, x):
    if x is self: return 1
    if len(self.item_) != len(x.item_): return 0
    for e1, e2 in zip(self.item_, x.item_):
      if e1 != e2: return 0
    if self.has_name_space_ != x.has_name_space_: return 0
    if self.has_name_space_ and self.name_space_ != x.name_space_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    for p in self.item_:
      if not p.IsInitialized(debug_strs): initialized=0
    return initialized

  def ByteSize(self):
    n = 0
    n += 2 * len(self.item_)
    for i in xrange(len(self.item_)): n += self.item_[i].ByteSize()
    if (self.has_name_space_): n += 1 + self.lengthString(len(self.name_space_))
    return n + 0

  def Clear(self):
    self.clear_item()
    self.clear_name_space()

  def OutputUnchecked(self, out):
    for i in xrange(len(self.item_)):
      out.putVarInt32(11)
      self.item_[i].OutputUnchecked(out)
      out.putVarInt32(12)
    if (self.has_name_space_):
      out.putVarInt32(58)
      out.putPrefixedString(self.name_space_)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 11:
        self.add_item().TryMerge(d)
        continue
      if tt == 58:
        self.set_name_space(d.getPrefixedString())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    cnt=0
    for e in self.item_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("Item%s {\n" % elm)
      res+=e.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
      cnt+=1
    if self.has_name_space_: res+=prefix+("name_space: %s\n" % self.DebugFormatString(self.name_space_))
    return res

  kItemGroup = 1
  kItemkey = 2
  kItemvalue = 3
  kItemflags = 4
  kItemset_policy = 5
  kItemexpiration_time = 6
  kname_space = 7

  _TEXT = (
   "ErrorCode",
   "Item",
   "key",
   "value",
   "flags",
   "set_policy",
   "expiration_time",
   "name_space",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.STARTGROUP,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.FLOAT,

   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.FLOAT,

   ProtocolBuffer.Encoder.STRING,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class MemcacheSetResponse(ProtocolBuffer.ProtocolMessage):

  STORED       =    1
  NOT_STORED   =    2
  ERROR        =    3

  _SetStatusCode_NAMES = {
    1: "STORED",
    2: "NOT_STORED",
    3: "ERROR",
  }

  def SetStatusCode_Name(cls, x): return cls._SetStatusCode_NAMES.get(x, "")
  SetStatusCode_Name = classmethod(SetStatusCode_Name)


  def __init__(self, contents=None):
    self.set_status_ = []
    if contents is not None: self.MergeFromString(contents)

  def set_status_size(self): return len(self.set_status_)
  def set_status_list(self): return self.set_status_

  def set_status(self, i):
    return self.set_status_[i]

  def set_set_status(self, i, x):
    self.set_status_[i] = x

  def add_set_status(self, x):
    self.set_status_.append(x)

  def clear_set_status(self):
    self.set_status_ = []


  def MergeFrom(self, x):
    assert x is not self
    for i in xrange(x.set_status_size()): self.add_set_status(x.set_status(i))

  def Equals(self, x):
    if x is self: return 1
    if len(self.set_status_) != len(x.set_status_): return 0
    for e1, e2 in zip(self.set_status_, x.set_status_):
      if e1 != e2: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    return initialized

  def ByteSize(self):
    n = 0
    n += 1 * len(self.set_status_)
    for i in xrange(len(self.set_status_)): n += self.lengthVarInt64(self.set_status_[i])
    return n + 0

  def Clear(self):
    self.clear_set_status()

  def OutputUnchecked(self, out):
    for i in xrange(len(self.set_status_)):
      out.putVarInt32(8)
      out.putVarInt32(self.set_status_[i])

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 8:
        self.add_set_status(d.getVarInt32())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    cnt=0
    for e in self.set_status_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("set_status%s: %s\n" % (elm, self.DebugFormatInt32(e)))
      cnt+=1
    return res

  kset_status = 1

  _TEXT = (
   "ErrorCode",
   "set_status",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.NUMERIC,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class MemcacheDeleteRequest_Item(ProtocolBuffer.ProtocolMessage):
  has_key_ = 0
  key_ = ""
  has_delete_time_ = 0
  delete_time_ = 0

  def __init__(self, contents=None):
    if contents is not None: self.MergeFromString(contents)

  def key(self): return self.key_

  def set_key(self, x):
    self.has_key_ = 1
    self.key_ = x

  def clear_key(self):
    if self.has_key_:
      self.has_key_ = 0
      self.key_ = ""

  def has_key(self): return self.has_key_

  def delete_time(self): return self.delete_time_

  def set_delete_time(self, x):
    self.has_delete_time_ = 1
    self.delete_time_ = x

  def clear_delete_time(self):
    if self.has_delete_time_:
      self.has_delete_time_ = 0
      self.delete_time_ = 0

  def has_delete_time(self): return self.has_delete_time_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_key()): self.set_key(x.key())
    if (x.has_delete_time()): self.set_delete_time(x.delete_time())

  def Equals(self, x):
    if x is self: return 1
    if self.has_key_ != x.has_key_: return 0
    if self.has_key_ and self.key_ != x.key_: return 0
    if self.has_delete_time_ != x.has_delete_time_: return 0
    if self.has_delete_time_ and self.delete_time_ != x.delete_time_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_key_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: key not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(len(self.key_))
    if (self.has_delete_time_): n += 5
    return n + 1

  def Clear(self):
    self.clear_key()
    self.clear_delete_time()

  def OutputUnchecked(self, out):
    out.putVarInt32(18)
    out.putPrefixedString(self.key_)
    if (self.has_delete_time_):
      out.putVarInt32(29)
      out.put32(self.delete_time_)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 12: break
      if tt == 18:
        self.set_key(d.getPrefixedString())
        continue
      if tt == 29:
        self.set_delete_time(d.get32())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_key_: res+=prefix+("key: %s\n" % self.DebugFormatString(self.key_))
    if self.has_delete_time_: res+=prefix+("delete_time: %s\n" % self.DebugFormatFixed32(self.delete_time_))
    return res

class MemcacheDeleteRequest(ProtocolBuffer.ProtocolMessage):
  has_name_space_ = 0
  name_space_ = ""

  def __init__(self, contents=None):
    self.item_ = []
    if contents is not None: self.MergeFromString(contents)

  def item_size(self): return len(self.item_)
  def item_list(self): return self.item_

  def item(self, i):
    return self.item_[i]

  def mutable_item(self, i):
    return self.item_[i]

  def add_item(self):
    x = MemcacheDeleteRequest_Item()
    self.item_.append(x)
    return x

  def clear_item(self):
    self.item_ = []
  def name_space(self): return self.name_space_

  def set_name_space(self, x):
    self.has_name_space_ = 1
    self.name_space_ = x

  def clear_name_space(self):
    if self.has_name_space_:
      self.has_name_space_ = 0
      self.name_space_ = ""

  def has_name_space(self): return self.has_name_space_


  def MergeFrom(self, x):
    assert x is not self
    for i in xrange(x.item_size()): self.add_item().CopyFrom(x.item(i))
    if (x.has_name_space()): self.set_name_space(x.name_space())

  def Equals(self, x):
    if x is self: return 1
    if len(self.item_) != len(x.item_): return 0
    for e1, e2 in zip(self.item_, x.item_):
      if e1 != e2: return 0
    if self.has_name_space_ != x.has_name_space_: return 0
    if self.has_name_space_ and self.name_space_ != x.name_space_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    for p in self.item_:
      if not p.IsInitialized(debug_strs): initialized=0
    return initialized

  def ByteSize(self):
    n = 0
    n += 2 * len(self.item_)
    for i in xrange(len(self.item_)): n += self.item_[i].ByteSize()
    if (self.has_name_space_): n += 1 + self.lengthString(len(self.name_space_))
    return n + 0

  def Clear(self):
    self.clear_item()
    self.clear_name_space()

  def OutputUnchecked(self, out):
    for i in xrange(len(self.item_)):
      out.putVarInt32(11)
      self.item_[i].OutputUnchecked(out)
      out.putVarInt32(12)
    if (self.has_name_space_):
      out.putVarInt32(34)
      out.putPrefixedString(self.name_space_)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 11:
        self.add_item().TryMerge(d)
        continue
      if tt == 34:
        self.set_name_space(d.getPrefixedString())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    cnt=0
    for e in self.item_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("Item%s {\n" % elm)
      res+=e.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
      cnt+=1
    if self.has_name_space_: res+=prefix+("name_space: %s\n" % self.DebugFormatString(self.name_space_))
    return res

  kItemGroup = 1
  kItemkey = 2
  kItemdelete_time = 3
  kname_space = 4

  _TEXT = (
   "ErrorCode",
   "Item",
   "key",
   "delete_time",
   "name_space",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.STARTGROUP,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.FLOAT,

   ProtocolBuffer.Encoder.STRING,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class MemcacheDeleteResponse(ProtocolBuffer.ProtocolMessage):

  DELETED      =    1
  NOT_FOUND    =    2

  _DeleteStatusCode_NAMES = {
    1: "DELETED",
    2: "NOT_FOUND",
  }

  def DeleteStatusCode_Name(cls, x): return cls._DeleteStatusCode_NAMES.get(x, "")
  DeleteStatusCode_Name = classmethod(DeleteStatusCode_Name)


  def __init__(self, contents=None):
    self.delete_status_ = []
    if contents is not None: self.MergeFromString(contents)

  def delete_status_size(self): return len(self.delete_status_)
  def delete_status_list(self): return self.delete_status_

  def delete_status(self, i):
    return self.delete_status_[i]

  def set_delete_status(self, i, x):
    self.delete_status_[i] = x

  def add_delete_status(self, x):
    self.delete_status_.append(x)

  def clear_delete_status(self):
    self.delete_status_ = []


  def MergeFrom(self, x):
    assert x is not self
    for i in xrange(x.delete_status_size()): self.add_delete_status(x.delete_status(i))

  def Equals(self, x):
    if x is self: return 1
    if len(self.delete_status_) != len(x.delete_status_): return 0
    for e1, e2 in zip(self.delete_status_, x.delete_status_):
      if e1 != e2: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    return initialized

  def ByteSize(self):
    n = 0
    n += 1 * len(self.delete_status_)
    for i in xrange(len(self.delete_status_)): n += self.lengthVarInt64(self.delete_status_[i])
    return n + 0

  def Clear(self):
    self.clear_delete_status()

  def OutputUnchecked(self, out):
    for i in xrange(len(self.delete_status_)):
      out.putVarInt32(8)
      out.putVarInt32(self.delete_status_[i])

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 8:
        self.add_delete_status(d.getVarInt32())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    cnt=0
    for e in self.delete_status_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("delete_status%s: %s\n" % (elm, self.DebugFormatInt32(e)))
      cnt+=1
    return res

  kdelete_status = 1

  _TEXT = (
   "ErrorCode",
   "delete_status",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.NUMERIC,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class MemcacheIncrementRequest(ProtocolBuffer.ProtocolMessage):

  INCREMENT    =    1
  DECREMENT    =    2

  _Direction_NAMES = {
    1: "INCREMENT",
    2: "DECREMENT",
  }

  def Direction_Name(cls, x): return cls._Direction_NAMES.get(x, "")
  Direction_Name = classmethod(Direction_Name)

  has_key_ = 0
  key_ = ""
  has_name_space_ = 0
  name_space_ = ""
  has_delta_ = 0
  delta_ = 1
  has_direction_ = 0
  direction_ = 1

  def __init__(self, contents=None):
    if contents is not None: self.MergeFromString(contents)

  def key(self): return self.key_

  def set_key(self, x):
    self.has_key_ = 1
    self.key_ = x

  def clear_key(self):
    if self.has_key_:
      self.has_key_ = 0
      self.key_ = ""

  def has_key(self): return self.has_key_

  def name_space(self): return self.name_space_

  def set_name_space(self, x):
    self.has_name_space_ = 1
    self.name_space_ = x

  def clear_name_space(self):
    if self.has_name_space_:
      self.has_name_space_ = 0
      self.name_space_ = ""

  def has_name_space(self): return self.has_name_space_

  def delta(self): return self.delta_

  def set_delta(self, x):
    self.has_delta_ = 1
    self.delta_ = x

  def clear_delta(self):
    if self.has_delta_:
      self.has_delta_ = 0
      self.delta_ = 1

  def has_delta(self): return self.has_delta_

  def direction(self): return self.direction_

  def set_direction(self, x):
    self.has_direction_ = 1
    self.direction_ = x

  def clear_direction(self):
    if self.has_direction_:
      self.has_direction_ = 0
      self.direction_ = 1

  def has_direction(self): return self.has_direction_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_key()): self.set_key(x.key())
    if (x.has_name_space()): self.set_name_space(x.name_space())
    if (x.has_delta()): self.set_delta(x.delta())
    if (x.has_direction()): self.set_direction(x.direction())

  def Equals(self, x):
    if x is self: return 1
    if self.has_key_ != x.has_key_: return 0
    if self.has_key_ and self.key_ != x.key_: return 0
    if self.has_name_space_ != x.has_name_space_: return 0
    if self.has_name_space_ and self.name_space_ != x.name_space_: return 0
    if self.has_delta_ != x.has_delta_: return 0
    if self.has_delta_ and self.delta_ != x.delta_: return 0
    if self.has_direction_ != x.has_direction_: return 0
    if self.has_direction_ and self.direction_ != x.direction_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_key_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: key not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(len(self.key_))
    if (self.has_name_space_): n += 1 + self.lengthString(len(self.name_space_))
    if (self.has_delta_): n += 1 + self.lengthVarInt64(self.delta_)
    if (self.has_direction_): n += 1 + self.lengthVarInt64(self.direction_)
    return n + 1

  def Clear(self):
    self.clear_key()
    self.clear_name_space()
    self.clear_delta()
    self.clear_direction()

  def OutputUnchecked(self, out):
    out.putVarInt32(10)
    out.putPrefixedString(self.key_)
    if (self.has_delta_):
      out.putVarInt32(16)
      out.putVarUint64(self.delta_)
    if (self.has_direction_):
      out.putVarInt32(24)
      out.putVarInt32(self.direction_)
    if (self.has_name_space_):
      out.putVarInt32(34)
      out.putPrefixedString(self.name_space_)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 10:
        self.set_key(d.getPrefixedString())
        continue
      if tt == 16:
        self.set_delta(d.getVarUint64())
        continue
      if tt == 24:
        self.set_direction(d.getVarInt32())
        continue
      if tt == 34:
        self.set_name_space(d.getPrefixedString())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_key_: res+=prefix+("key: %s\n" % self.DebugFormatString(self.key_))
    if self.has_name_space_: res+=prefix+("name_space: %s\n" % self.DebugFormatString(self.name_space_))
    if self.has_delta_: res+=prefix+("delta: %s\n" % self.DebugFormatInt64(self.delta_))
    if self.has_direction_: res+=prefix+("direction: %s\n" % self.DebugFormatInt32(self.direction_))
    return res

  kkey = 1
  kname_space = 4
  kdelta = 2
  kdirection = 3

  _TEXT = (
   "ErrorCode",
   "key",
   "delta",
   "direction",
   "name_space",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.STRING,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class MemcacheIncrementResponse(ProtocolBuffer.ProtocolMessage):
  has_new_value_ = 0
  new_value_ = 0

  def __init__(self, contents=None):
    if contents is not None: self.MergeFromString(contents)

  def new_value(self): return self.new_value_

  def set_new_value(self, x):
    self.has_new_value_ = 1
    self.new_value_ = x

  def clear_new_value(self):
    if self.has_new_value_:
      self.has_new_value_ = 0
      self.new_value_ = 0

  def has_new_value(self): return self.has_new_value_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_new_value()): self.set_new_value(x.new_value())

  def Equals(self, x):
    if x is self: return 1
    if self.has_new_value_ != x.has_new_value_: return 0
    if self.has_new_value_ and self.new_value_ != x.new_value_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    return initialized

  def ByteSize(self):
    n = 0
    if (self.has_new_value_): n += 1 + self.lengthVarInt64(self.new_value_)
    return n + 0

  def Clear(self):
    self.clear_new_value()

  def OutputUnchecked(self, out):
    if (self.has_new_value_):
      out.putVarInt32(8)
      out.putVarUint64(self.new_value_)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 8:
        self.set_new_value(d.getVarUint64())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_new_value_: res+=prefix+("new_value: %s\n" % self.DebugFormatInt64(self.new_value_))
    return res

  knew_value = 1

  _TEXT = (
   "ErrorCode",
   "new_value",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.NUMERIC,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class MemcacheFlushRequest(ProtocolBuffer.ProtocolMessage):

  def __init__(self, contents=None):
    pass
    if contents is not None: self.MergeFromString(contents)


  def MergeFrom(self, x):
    assert x is not self

  def Equals(self, x):
    if x is self: return 1
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    return initialized

  def ByteSize(self):
    n = 0
    return n + 0

  def Clear(self):
    pass

  def OutputUnchecked(self, out):
    pass

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    return res


  _TEXT = (
   "ErrorCode",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class MemcacheFlushResponse(ProtocolBuffer.ProtocolMessage):

  def __init__(self, contents=None):
    pass
    if contents is not None: self.MergeFromString(contents)


  def MergeFrom(self, x):
    assert x is not self

  def Equals(self, x):
    if x is self: return 1
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    return initialized

  def ByteSize(self):
    n = 0
    return n + 0

  def Clear(self):
    pass

  def OutputUnchecked(self, out):
    pass

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    return res


  _TEXT = (
   "ErrorCode",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class MemcacheStatsRequest(ProtocolBuffer.ProtocolMessage):

  def __init__(self, contents=None):
    pass
    if contents is not None: self.MergeFromString(contents)


  def MergeFrom(self, x):
    assert x is not self

  def Equals(self, x):
    if x is self: return 1
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    return initialized

  def ByteSize(self):
    n = 0
    return n + 0

  def Clear(self):
    pass

  def OutputUnchecked(self, out):
    pass

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    return res


  _TEXT = (
   "ErrorCode",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class MergedNamespaceStats(ProtocolBuffer.ProtocolMessage):
  has_hits_ = 0
  hits_ = 0
  has_misses_ = 0
  misses_ = 0
  has_byte_hits_ = 0
  byte_hits_ = 0
  has_items_ = 0
  items_ = 0
  has_bytes_ = 0
  bytes_ = 0
  has_oldest_item_age_ = 0
  oldest_item_age_ = 0

  def __init__(self, contents=None):
    if contents is not None: self.MergeFromString(contents)

  def hits(self): return self.hits_

  def set_hits(self, x):
    self.has_hits_ = 1
    self.hits_ = x

  def clear_hits(self):
    if self.has_hits_:
      self.has_hits_ = 0
      self.hits_ = 0

  def has_hits(self): return self.has_hits_

  def misses(self): return self.misses_

  def set_misses(self, x):
    self.has_misses_ = 1
    self.misses_ = x

  def clear_misses(self):
    if self.has_misses_:
      self.has_misses_ = 0
      self.misses_ = 0

  def has_misses(self): return self.has_misses_

  def byte_hits(self): return self.byte_hits_

  def set_byte_hits(self, x):
    self.has_byte_hits_ = 1
    self.byte_hits_ = x

  def clear_byte_hits(self):
    if self.has_byte_hits_:
      self.has_byte_hits_ = 0
      self.byte_hits_ = 0

  def has_byte_hits(self): return self.has_byte_hits_

  def items(self): return self.items_

  def set_items(self, x):
    self.has_items_ = 1
    self.items_ = x

  def clear_items(self):
    if self.has_items_:
      self.has_items_ = 0
      self.items_ = 0

  def has_items(self): return self.has_items_

  def bytes(self): return self.bytes_

  def set_bytes(self, x):
    self.has_bytes_ = 1
    self.bytes_ = x

  def clear_bytes(self):
    if self.has_bytes_:
      self.has_bytes_ = 0
      self.bytes_ = 0

  def has_bytes(self): return self.has_bytes_

  def oldest_item_age(self): return self.oldest_item_age_

  def set_oldest_item_age(self, x):
    self.has_oldest_item_age_ = 1
    self.oldest_item_age_ = x

  def clear_oldest_item_age(self):
    if self.has_oldest_item_age_:
      self.has_oldest_item_age_ = 0
      self.oldest_item_age_ = 0

  def has_oldest_item_age(self): return self.has_oldest_item_age_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_hits()): self.set_hits(x.hits())
    if (x.has_misses()): self.set_misses(x.misses())
    if (x.has_byte_hits()): self.set_byte_hits(x.byte_hits())
    if (x.has_items()): self.set_items(x.items())
    if (x.has_bytes()): self.set_bytes(x.bytes())
    if (x.has_oldest_item_age()): self.set_oldest_item_age(x.oldest_item_age())

  def Equals(self, x):
    if x is self: return 1
    if self.has_hits_ != x.has_hits_: return 0
    if self.has_hits_ and self.hits_ != x.hits_: return 0
    if self.has_misses_ != x.has_misses_: return 0
    if self.has_misses_ and self.misses_ != x.misses_: return 0
    if self.has_byte_hits_ != x.has_byte_hits_: return 0
    if self.has_byte_hits_ and self.byte_hits_ != x.byte_hits_: return 0
    if self.has_items_ != x.has_items_: return 0
    if self.has_items_ and self.items_ != x.items_: return 0
    if self.has_bytes_ != x.has_bytes_: return 0
    if self.has_bytes_ and self.bytes_ != x.bytes_: return 0
    if self.has_oldest_item_age_ != x.has_oldest_item_age_: return 0
    if self.has_oldest_item_age_ and self.oldest_item_age_ != x.oldest_item_age_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_hits_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: hits not set.')
    if (not self.has_misses_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: misses not set.')
    if (not self.has_byte_hits_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: byte_hits not set.')
    if (not self.has_items_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: items not set.')
    if (not self.has_bytes_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: bytes not set.')
    if (not self.has_oldest_item_age_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: oldest_item_age not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthVarInt64(self.hits_)
    n += self.lengthVarInt64(self.misses_)
    n += self.lengthVarInt64(self.byte_hits_)
    n += self.lengthVarInt64(self.items_)
    n += self.lengthVarInt64(self.bytes_)
    return n + 10

  def Clear(self):
    self.clear_hits()
    self.clear_misses()
    self.clear_byte_hits()
    self.clear_items()
    self.clear_bytes()
    self.clear_oldest_item_age()

  def OutputUnchecked(self, out):
    out.putVarInt32(8)
    out.putVarUint64(self.hits_)
    out.putVarInt32(16)
    out.putVarUint64(self.misses_)
    out.putVarInt32(24)
    out.putVarUint64(self.byte_hits_)
    out.putVarInt32(32)
    out.putVarUint64(self.items_)
    out.putVarInt32(40)
    out.putVarUint64(self.bytes_)
    out.putVarInt32(53)
    out.put32(self.oldest_item_age_)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 8:
        self.set_hits(d.getVarUint64())
        continue
      if tt == 16:
        self.set_misses(d.getVarUint64())
        continue
      if tt == 24:
        self.set_byte_hits(d.getVarUint64())
        continue
      if tt == 32:
        self.set_items(d.getVarUint64())
        continue
      if tt == 40:
        self.set_bytes(d.getVarUint64())
        continue
      if tt == 53:
        self.set_oldest_item_age(d.get32())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_hits_: res+=prefix+("hits: %s\n" % self.DebugFormatInt64(self.hits_))
    if self.has_misses_: res+=prefix+("misses: %s\n" % self.DebugFormatInt64(self.misses_))
    if self.has_byte_hits_: res+=prefix+("byte_hits: %s\n" % self.DebugFormatInt64(self.byte_hits_))
    if self.has_items_: res+=prefix+("items: %s\n" % self.DebugFormatInt64(self.items_))
    if self.has_bytes_: res+=prefix+("bytes: %s\n" % self.DebugFormatInt64(self.bytes_))
    if self.has_oldest_item_age_: res+=prefix+("oldest_item_age: %s\n" % self.DebugFormatFixed32(self.oldest_item_age_))
    return res

  khits = 1
  kmisses = 2
  kbyte_hits = 3
  kitems = 4
  kbytes = 5
  koldest_item_age = 6

  _TEXT = (
   "ErrorCode",
   "hits",
   "misses",
   "byte_hits",
   "items",
   "bytes",
   "oldest_item_age",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.FLOAT,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class MemcacheStatsResponse(ProtocolBuffer.ProtocolMessage):
  has_stats_ = 0
  stats_ = None

  def __init__(self, contents=None):
    self.lazy_init_lock_ = thread.allocate_lock()
    if contents is not None: self.MergeFromString(contents)

  def stats(self):
    if self.stats_ is None:
      self.lazy_init_lock_.acquire()
      try:
        if self.stats_ is None: self.stats_ = MergedNamespaceStats()
      finally:
        self.lazy_init_lock_.release()
    return self.stats_

  def mutable_stats(self): self.has_stats_ = 1; return self.stats()

  def clear_stats(self):
    if self.has_stats_:
      self.has_stats_ = 0;
      if self.stats_ is not None: self.stats_.Clear()

  def has_stats(self): return self.has_stats_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_stats()): self.mutable_stats().MergeFrom(x.stats())

  def Equals(self, x):
    if x is self: return 1
    if self.has_stats_ != x.has_stats_: return 0
    if self.has_stats_ and self.stats_ != x.stats_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (self.has_stats_ and not self.stats_.IsInitialized(debug_strs)): initialized = 0
    return initialized

  def ByteSize(self):
    n = 0
    if (self.has_stats_): n += 1 + self.lengthString(self.stats_.ByteSize())
    return n + 0

  def Clear(self):
    self.clear_stats()

  def OutputUnchecked(self, out):
    if (self.has_stats_):
      out.putVarInt32(10)
      out.putVarInt32(self.stats_.ByteSize())
      self.stats_.OutputUnchecked(out)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 10:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.mutable_stats().TryMerge(tmp)
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_stats_:
      res+=prefix+"stats <\n"
      res+=self.stats_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
    return res

  kstats = 1

  _TEXT = (
   "ErrorCode",
   "stats",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.STRING,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""

__all__ = ['MemcacheServiceError','MemcacheGetRequest','MemcacheGetResponse','MemcacheGetResponse_Item','MemcacheSetRequest','MemcacheSetRequest_Item','MemcacheSetResponse','MemcacheDeleteRequest','MemcacheDeleteRequest_Item','MemcacheDeleteResponse','MemcacheIncrementRequest','MemcacheIncrementResponse','MemcacheFlushRequest','MemcacheFlushResponse','MemcacheStatsRequest','MergedNamespaceStats','MemcacheStatsResponse']
