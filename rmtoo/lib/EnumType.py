'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Enum type
   Because python lacks the enum construct, this is a way to reinvent
   it.

 (c) 2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


def EnumType(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('EnumType', (), enums)
