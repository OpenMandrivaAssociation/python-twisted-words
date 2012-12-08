%define name python-twisted-words
%define version 12.2.0
%define rel 1
%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

Summary:        Chat and Instant Messaging module for Twisted
Name:           %{name}
Version:	%{version}
Release:	%mkrel %{rel}
Source0:        http://twistedmatrix.com/Releases/Words/%{mainver}/TwistedWords-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/trac/wiki/TwistedWords
BuildRequires:	python-devel python-twisted-core
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



%files
%defattr(0644,root,root,0755)
%doc LICENSE NEWS README doc/*
%dir %py_platsitedir/twisted/words/
%py_platsitedir/twisted/words/*
%py_platsitedir/twisted/plugins/*
%py_platsitedir/*.egg-info
