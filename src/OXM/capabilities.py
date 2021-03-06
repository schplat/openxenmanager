# -----------------------------------------------------------------------
# OpenXenManager
#
# Copyright (C) 2009 Alberto Gonzalez Rodriguez alberto@pesadilla.org
# Copyright (C) 2011 Cheng Sun <chengsun9@gmail.com>
# Copyright (C) 2014 Daniel Lintott <daniel@serverb.co.uk>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# -----------------------------------------------------------------------
capabilities_conf_text = ["These files will contain personally identifiable information",
                          "These files may contain personally identifiable information",
                          "These files may contain personally identifiable information if customized",
                          "These files will contain no personally identifiable information"
                          ]

capabilities_text = {"host-crashdump-dumps": ["Crash dump files", "Memory dump created on server crash, if you select "
                                                                  "this option you will be prompted for these files to "
                                                                  "be removed after the report has been compiled"],
                     "firstboot": ["First-boot scripts", "The scripts run for initializing local storage repositories "
                                                         "and networking"],
                     "network-status": ["Network status", "Current status of the network interfaces, routing tables and"
                                                          " firewall"],
                     "process-list": ["Process listing", "A complete listing of the processes running in a tree "
                                                         "format"],
                     "xenserver-databases": ["XenServer database", "The database which stores the state of the "
                                                                   "XenServer"],
                     "disk-info": ["Disk information", "Partition tables, free space, iSCSI and LVM configuration"],
                     "hardware-info": ["Hardware information", "Details of the processors, memory and other basic "
                                                               "hardware"],
                     "high-availability": ["Hight availability", "Log file from the high availability daemon"],
                     "xha-liveset": ["High availability liveset", "High availability liveset"],
                     "xen-info": ["Hypervisor configuration", "Details of the hypervisor version and its current "
                                                              "state"],
                     "kernel-info": ["Kernel information", "Details of kernel modules, filesystems devices and kernel "
                                                           "configuration"],
                     "loopback-devices": ["Loopback devices", "Details of loopback devices"],
                     "multipath": ["Multipathing configuration", "Retrieves the server's storage multipathing "
                                                                 "configuration"],
                     "persistent-stats": ["Persistent statistics", "Persistent performance statistics"],
                     "system-logs": ["System logs", "Logfiles which record the activity of various system processes"],
                     "vncterm": ["VNCTerm crash dumps", "Crash dumps files from the VNCTerm daemon"],
                     "xenserver-config": ["XenServer Configuration", "Details of the XenServer such as version and "
                                                                     "build information, primary hard disk location "
                                                                     "and pool configuration"],
                     "xapi-debug": ["XenServer daemon crash dumps", "XenServer daemon crash dumps"],
                     "xenserver-install": ["XenServer installation log files", "Log files generated during the "
                                                                               "installation of the XenServer"],
                     "xenserver-logs": ["Xenserver logs", "Log files concerning the XenServer's activity"],
                     "network-config": ["Network scripts", "Configuration files used to bring up network interfaces, "
                                                           "provide name resolution and enable the firewall"],
                     "yum": ["RPM package database", "YUM repository information and RPM package database listing"],
                     "pam": ["Authentication module configuration", ""],
                     "boot-loader": ["Boot loader configuration", "List of boot options and their details given to the "
                                                                  "user at system boot time"],
                     "CVSM": ["Citrix StorageLink configuration", "The configuration settings of Citrix StorageLink"],
                     "host-crashdump-logs": ["Crash dump logs", "Log files generated at time of server crash"],
                     "hdparm-t": ["Local performance test", "Performs a number of timing tests on each local hard "
                                                            "disk, these may take up to one minute to complete"],
                     "tapdisk-logs": ["Storage subsystem logs", "Storage subsystem logs"],
                     "system-services": ["System services", "A listing of configured system services"],
                     "blobs": ["User-created binary objects", ""],
                     "wlb": ["Workload Balancing status", "Logs and status information from the WLB server monitoring "
                                                          "this pool."],
                     "X11": ["X server logs", "Log files from the X server"],
                     "X11-auth": ["X11 authority", "X server authority files"],
                     "xapi-subprocess": ["Xenserver daemon subprocesses", "XenServer daemon process details"],
                     "xenserver-domains": ["XenServer domains list", "List of the guest VMs installed onto the server "
                                                                     "and their current states"]}