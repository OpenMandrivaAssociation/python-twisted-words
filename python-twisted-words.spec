%define name python-twisted-words
%define version 10.1.0
%define rel 1
%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

Summary:        Chat and Instant Messaging module for Twisted
Name:           %{name}
Version:	%{version}
Release:	%mkrel %{rel}
Source0:        http://tmrc.mit.edu/mirror/twisted/Words/%{mainver}/TwistedWords-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/trac/wiki/TwistedWords
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel python-twisted-core
#BuildArch:      noarch
Requires:       python-twisted-core
# for words/tap.py
Requires:       python-twisted-web

%description
Twisted Words includes:

* Low-level protocol implementations of OSCAR (AIM and ICQ), IRC, MSN,
  TOC (AIM).
* Jabber libraries.
* Prototypes of chat server and client frameworks built on top of
  the protocols.

%prep
%setup -q -n TwistedWords-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir}

%__install -d                      %buildroot%_mandir/man1
%__install -m 644 doc/man/*.1      %buildroot%_mandir/man1

%clean
%__rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc LICENSE NEWS README doc/*
%dir %py_platsitedir/twisted/words/
%py_platsitedir/twisted/words/*
%py_platsitedir/twisted/plugins/*
%py_platsitedir/*.egg-info
%_mandir/man1/*

