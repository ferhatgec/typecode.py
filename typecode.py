# MIT License
#
# Copyright (c) 2021 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
# typecode[dot]py - An interpreter that introduces you.
#
# An example code:
#  $%#/*++;%##*++;#/++++;#/*++;#/*+++;-%##*;$@/*+;+++;#/;@
#
# Output:
#  Languages:
#      FlaScript
#      Gretea
#      C
#      C++
#      C++/CLI
#      Python
#
#  Branches:
#      Computer Science
#      Programming languages
#      Programming languages and compilers
#
# github.com/ferhatgec/typecode.py
# github.com/ferhatgec/typecode

class Tokens:
    Lang = '$'
    Branch = '@'
    OS = '?'

    Push = '+'
    Push5 = '*'
    Push10 = '/'
    Push50 = '%'
    Push100 = '-'
    Print = ';'


class TypeCode:
    def __init__(self):
        # taken from https://dzone.com/articles/big-list-256-programming
        self.__languages = []

        # taken from https://www.quora.com/What-are-the-branches-of-computer-science
        self.__branches = []

        self.__operating_systems = []

        self.__data: str = ''
        self.__is_language, \
            self.__is_branch,\
            self.__is_os = False, False, False

        self.__stack = 0

        self.info_languages = []
        self.info_branches = []
        self.info_operating_systems = []

    def init(self, file_data: str):
        self.init_languages()
        self.init_branches()
        self.init_operating_systems()

        for ch in file_data:
            # $+++++++;+++;$
            #
            # @+++++++++++++++;@
            if ch == Tokens.Lang: self.__is_language = not self.__is_language
            elif ch == Tokens.Branch: self.__is_branch = not self.__is_branch
            elif ch == Tokens.OS: self.__is_os = not self.__is_os
            elif ch == Tokens.Push: self.__stack += 1
            elif ch == Tokens.Push5: self.__stack += 5
            elif ch == Tokens.Push10: self.__stack += 10
            elif ch == Tokens.Push50: self.__stack += 50
            elif ch == Tokens.Push100: self.__stack += 100
            elif ch == Tokens.Print:
                if self.__is_branch and self.__stack < len(self.__branches):
                    self.info_branches.append(self.__branches[self.__stack])
                elif self.__is_language and self.__stack < len(self.__languages):
                    self.info_languages.append(self.__languages[self.__stack])
                elif self.__is_os and self.__stack < len(self.__operating_systems):
                    self.info_operating_systems.append(self.__operating_systems[self.__stack])

                self.__stack = 0

    def init_languages(self):
        self.__languages = [
            '4th Dimension/4D',
            'ABAP',
            'ABC',
            'ActionScript',
            'Ada',
            'Agilent VEE',
            'Algol',
            'Alice',
            'Angelscript',
            'Apex',
            'APL',
            'AppleScript',
            'Arc',
            'Arduino',
            'ASP',
            'AspectJ',
            'Assembly',
            'ATLAS',
            'Augeas',
            'AutoHotkey',
            'AutoIt',
            'AutoLISP',
            'Automator',
            'Avenue',
            'Awk',
            'Bash',
            '(Visual) Basic',
            'bc',
            'BCPL',
            'BETA',
            'BlitzMax',
            'Boo',
            'Bourne Shell',
            'Bro',
            'C',
            'C Shell',
            'C#',
            'C++',
            'C++/CLI',
            'C-Omega',
            'Caml',
            'Ceylon',
            'CFML',
            'cg',
            'Ch',
            'CHILL',
            'CIL',
            'CL (OS/400)',
            'Clarion',
            'Clean',
            'Clipper',
            'Clojure',
            'CLU',
            'COBOL',
            'Cobra',
            'CoffeeScript',
            'ColdFusion',
            'COMAL',
            'Common Lisp',
            'Coq',
            'cT',
            'Curl',
            'D',
            'Dart',
            'DCL',
            'DCPU-16 ASM',
            'Delphi/Object Pascal',
            'DiBOL',
            'Dylan',
            'E',
            'eC',
            'Ecl',
            'ECMAScript',
            'EGL',
            'Eiffel',
            'Elixir',
            'Emacs Lisp',
            'Erlang',
            'Etoys',
            'Euphoria',
            'EXEC',
            'F#',
            'Factor',
            'Falcon',
            'Fancy',
            'Fantom',
            'Felix',
            'FlaScript',
            'Forth',
            'Fortran',
            'Fortress',
            '(Visual) FoxPro',
            'Gambas',
            'GNU Octave',
            'Go',
            'Google AppsScript',
            'Gosu',
            'Gretea',
            'Groovy',
            'Haskell',
            'haXe',
            'Heron',
            'HPL',
            'HyperTalk',
            'Icon',
            'IDL',
            'Inform',
            'Informix-4GL',
            'INTERCAL',
            'Io',
            'Ioke',
            'J',
            'J#',
            'JADE',
            'Java',
            'Java FX Script',
            'JavaScript',
            'JScript',
            'JScript.NET',
            'Julia',
            'Korn Shell',
            'Kotlin',
            'LabVIEW',
            'Ladder Logic',
            'Lasso',
            'Limbo',
            'Lingo',
            'Lisp',
            'Logo',
            'Logtalk',
            'LotusScript',
            'LPC',
            'Lua',
            'Lustre',
            'M4',
            'MAD',
            'Magic',
            'Magik',
            'Malbolge',
            'MANTIS',
            'Maple',
            'Mathematica',
            'MATLAB',
            'Max/MSP',
            'MAXScript',
            'MEL',
            'Mercury',
            'Mirah',
            'Miva',
            'ML',
            'Monkey',
            'Modula-2',
            'Modula-3',
            'MOO',
            'Moto',
            'MS-DOS Batch',
            'MUMPS',
            'NATURAL',
            'Nemerle',
            'Nim',
            'NQC',
            'NSIS',
            'Nu',
            'NXT-G',
            'Oberon',
            'Object Rexx',
            'Objective-C',
            'Objective-J',
            'OCaml',
            'Occam',
            'ooc',
            'Opa',
            'OpenCL',
            'OpenEdge ABL',
            'OPL',
            'Oz',
            'Paradox',
            'Parrot',
            'Pascal',
            'Perl',
            'PHP',
            'Pike',
            'PILOT',
            'PL/I',
            'PL/SQL',
            'Pliant',
            'PostScript',
            'POV-Ray',
            'PowerBasic',
            'PowerScript',
            'PowerShell',
            'Processing',
            'Prolog',
            'Puppet',
            'Pure Data',
            'Python',
            'Q',
            'R',
            'Racket',
            'REALBasic',
            'REBOL',
            'Revolution',
            'REXX',
            'RPG (OS/400)',
            'Ruby',
            'Rust',
            'S',
            'S-PLUS',
            'SAS',
            'Sather',
            'Scala',
            'Scheme',
            'Scilab',
            'Scratch',
            'sed',
            'Seed7',
            'Self',
            'Shell',
            'SIGNAL',
            'Simula',
            'Simulink',
            'Slate',
            'Smalltalk',
            'Smarty',
            'SPARK',
            'SPSS',
            'SQR',
            'Squeak',
            'Squirrel',
            'Standard ML',
            'Suneido',
            'SuperCollider',
            'TACL',
            'Tcl',
            'Tex',
            'thinBasic',
            'TOM',
            'Transact-SQL',
            'Turing',
            'TypeScript',
            'Vala/Genie',
            'VBScript',
            'Verilog',
            'VHDL',
            'VimL',
            'Visual Basic .NET',
            'WebDNA',
            'Whitespace',
            'X10',
            'xBase',
            'XBase++',
            'Xen',
            'XPL',
            'XSLT',
            'XQuery',
            'yacc',
            'Yorick',
            'Z shell'
        ]

    def init_branches(self):
        self.__branches = [
            'Human-computer interaction',
            'Data science',
            'Natural language processing',
            'Programming languages',
            'Software engineering',
            'Architecture and organization',
            'Cyber security',
            'Information management',
            'Networking and communication',
            'Computer graphics',
            'Platform-based development',
            'Graphics and visual computing',
            'Algorithms and complexity',
            'Parallel and distributed computing',
            'Intelligent systems',
            'Security and information assurance',
            'Computer Science',
            'Computer Engineering',
            'Information Systems',
            'New Media',
            'Information Technology (IT)',
            'Information Science',
            'Mathematical foundations.',
            'Algorithms and data structures.',
            'Artificial intelligence.',
            'Communication and security.',
            'Computer architecture.',
            'Computer graphics.',
            'Concurrent, parallel, and distributed systems.',
            'Databases.',
            'Programming languages and compilers',
            'Scientific computing',
            'Software engineering',
            'Theory of computing'
        ]

    def init_operating_systems(self):
        self.__operating_systems = [
            'Arthur',
            'RISC OS',
            'Fire OS',
            'Amiga OS',
            'AMSDOS',
            'macOS',
            'iOS',
            'iPadOS',
            'tvOS',
            'bridgeOS',
            'Atari DOS',
            'BeOS',
            'Unix',
            'BESYS',
            'Plan 9',
            'Inferno',
            'Android',
            'Harmony OS',
            'LiteOS',
            'iRMX',
            'PC DOS',
            'OS/2',
            'Remix OS',
            'KaiOS',
            'LynxOS',
            'Xenix',
            'MS-DOS',
            'DOS/V',
            'Windows',
                'Windows 1.0',
                'Windows 2.0',
                'Windows 3.0',
                'Windows 3.1x',
                'Windows 3.2',
                'Windows 95',
                'Windows 98',
                'Windows ME',

                'Windows NT',
                    'Windows NT 3.1',
                    'Windows NT 4.0',
                    'Windows 2000',
                    'Windows XP',
                    'Windows Server 2003',
                    'Windows Vista',
                    'Windows Phone 7',
                    'Windows 8',
                    'Windows RT',
                    'Windows Phone 8',
                    'Windows 8.1',
                    'Windows Phone 8.1',
                    'Windows 10',
                    'Windows 10 Mobile',
                    'Windows 11',
            'ES',
            'NeXTSTEP',
            'NetWare',
            'UnixWare',
            'Bada',
            'Tizen',
            'One UI',
            'Sun OS',
            'Solaris'
            'BSD',
                'FreeBSD',
                    'DragonFlyBSD',
                    'MidnightBSD',
                    'GhostBSD',
                    'TrueOS',
                    'prismBSD',
                'NetBSD',
                    'OpenBSD',
                        'Bitrig',
                'Darwin',

            'GNU Hurd',
            'Linux',
                'RHEL',
                    'Rocky Linux'
                'RPM',
                    'Red Hat Linux',
                    'CentOS',
                    'Fedora',
                        'Qubes OS'
                    'openSUSE',
                        'SUSE Linux Enterprise Desktop',
                        'SUSE Linux Enterprise Server',
                        'SUSE Studio',
                        'GeckoLinux',
                    'Mandrake Linux',
                'Debian',
                    'MX Linux',
                    'Deepin',
                    'Devuan',
                    'Kali Linux',
                    'Pure OS',
                    'Ubuntu',
                        'Kubuntu',
                        'Lubuntu',
                        'Ubuntu Budgie',
                        'Ubuntu Kylin',
                        'Ubuntu Mate',
                        'Xubuntu',

                        'Bodhi Linux',
                        'elementary OS',
                        'Linux Mint',
                        'Zorin OS',
                        'Pop!_OS',

                'Arch Linux',
                    'Manjaro',
                    'Artix Linux',
                    'EndeavourOS',
                    'SteamOS',
                'Gentoo',
                    'Chrome OS',
                    'Chromium OS',
                'NixOS',
                'Void Linux',
                'GuixSD',
                'Solus',
            'Redox',
            'illumos',
                'OpenIndiana',

            'FreeDOS',
            'Genode',
            'FFusionOS',
            'Ghost OS',
            'Haiku',
            'ReactOS',
            'TempleOS',
            'Serenity',
            'Visopsys'
        ]