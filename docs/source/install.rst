+++++++++++++++++++++++
Installing Quark-Engine
+++++++++++++++++++++++

PyPi::

    $ pip3 install -U quark-engine

Install from Source::

    $ git clone https://github.com/quark-engine/quark-engine.git
    $ cd quark-engine/
    $ pipenv install --skip-lock
    $ pipenv shell

Run the help cmd of quark::

    $ quark --help

Once you see the following msg, then you're all set::

    Usage: quark [OPTIONS]

    Quark is an Obfuscation-Neglect Android Malware Scoring System

    Options:
      -s, --summary TEXT              Show summary report
      -d, --detail TEXT               Show detail report
      -o, --output FILE               Output report in JSON
      -a, --apk FILE                  APK file  [required]
      -r, --rule PATH                 Rules directory  [default:
                                      /Users/nick/.quark-engine/quark-rules]
      -g, --graph                     Create call graph to call_graph_image
                                      directory
      -c, --classification            Show rules classification
      -t, --threshold [100|80|60|40|20]
                                      Set the confidence threshold
      -i, --list [all|native|custom]  List classes, methods and descriptors
      -p, --permission                List Android permissions
      -l, --label [max|detailed]      Show report based on label of rules
      --help                          Show this message and exit.

To learn how to scan multiple samples in a directory, please have a look at :ref:`Directory Scanning <dir_scan>`
