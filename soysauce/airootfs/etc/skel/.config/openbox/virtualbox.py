import sys
import os

def get_base_prefix_compat():
    """Get base/real prefix, or sys.prefix if there is none."""
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

def in_virtualenv():
    return get_base_prefix_compat() != sys.prefix

if in_virtualenv() == True:
    os.system ("VBoxClient --clipboard &")
    os.system ("VBoxClient --draganddrop &")
    os.system ("VBoxClient --seamless &")
    os.system ("VBoxClient --checkhostversion &")
    os.system ("VBoxClient --vmsvga &")
