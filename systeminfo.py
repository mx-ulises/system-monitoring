#!/bin/python
"""
================================================================================
                              DESCRIPTION
================================================================================

  This script reports in a human-readable way the status of the system based in
  the predefined reporting-structure and  configuration files.

================================================================================
                              MAINTAINERS
================================================================================

  This section contains all the maintainers primary information to get track of
  the contributors to this code in the file. The maintainer's list contains a
  maintainer alias (required), his name (optional) and contact mails (one
  required).


  Alias     Name              Mail
--------------------------------------------------------------------------------
  ulisesma  Ulises Martinez   ulises.martinezaraiza.mx@ieee.org
                              umartinez@gdl.cinvestav.mx


================================================================================
                              CHANGE LOG
================================================================================

      Version: 0.1
  Last Update: 2016-08-02

  Date        Alias      Description
--------------------------------------------------------------------------------
  2016-08-02  ulisesma   Initial file creation

"""
"""
================================================================================
                              Imports and Globals
================================================================================
"""
from time import strftime
import report_colors
import collections
Entry = collections.namedtuple('Entry', 'desc state')

""" Global """
MAIN_SEPARATOR_BAR = "================================================================================"
LESS_SEPARATOR_BAR = "--------------------------------------------------------------------------------"
LINE_WIDTH = 80
DESC_WIDTH = 60

""" Mock values """
SYSTEM_NAME = "House IoT Monitoring"
SYSTEM_VER = "1.1.2"
SYSTEM_GENERIC_DATE = strftime("%Y-%m-%d %H:%M:%S")
SYSTEM_CMP = "5"
VERBOSE = False
GENERAL_STATE = Entry(desc="General Current State:",
                      state=report_colors.ok("NORMAL"))

"""
================================================================================
                              Functions
================================================================================
"""

def report_state(entry):
    return "{0}{1}".format(entry.desc.ljust(DESC_WIDTH), entry.state)

def print_header(system_object):
    print MAIN_SEPARATOR_BAR
    print "System Info report for {0}".format(SYSTEM_NAME).center(LINE_WIDTH)
    width = LINE_WIDTH / 2
    print MAIN_SEPARATOR_BAR
    version = "Version: {0}".format(SYSTEM_VER)
    component = "Components: {0}".format(SYSTEM_CMP)
    state = report_state(GENERAL_STATE)
    start_date = "Start Date:   {0}".format(SYSTEM_GENERIC_DATE)
    failure_date = "Last Failure: {0}".format(SYSTEM_GENERIC_DATE)
    update_date = "Last Update:  {0}".format(SYSTEM_GENERIC_DATE)
    current_date = "Current Date: {0}".format(strftime("%Y-%m-%d %H:%M:%S"))
    print state
    print LESS_SEPARATOR_BAR
    print "{0}{1}".format(version.ljust(width), start_date.ljust(width))
    print "{0}{1}".format(component.ljust(width), failure_date.ljust(width))
    print "{0}{1}".format("".ljust(width), update_date.ljust(width))
    print "{0}{1}".format("".ljust(width), current_date.ljust(width))
    print MAIN_SEPARATOR_BAR


def print_component(system_component):
    pass


"""
================================================================================
                              Main Flow
================================================================================
"""
""" Precompute """
system_object = None
components = []

""" Program flow """
print_header(system_object)
for system_component in components:
    print_component(system_component)
