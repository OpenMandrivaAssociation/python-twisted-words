# There is no debug here, but can't build as noarch,
# since some 'twisted' modules are arch-dependent and all these modules
# should be located in the same place
%define debug_package %{nil}

%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

Summary:	Chat and Instant Messaging module for Twisted

Name:		python-twisted-words
Version:	14.0.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		http://twistedmatrix.com/trac/wiki/TwistedWords
Source0:	http://twistedmatrix.com/Releases/Words/14.0/TwistedWords-%{version}.tar.bz2
BuildRequires:	python-twisted-core
BuildRequires:	pkgconfig(python)
Requires:	python-twisted-core
# for words/tap.py
Requires:	python-twisted-web

%description
Twisted Words includes:

* Low-level protocol implementations of OSCAR (AIM and ICQ), IRC, MSN,
  TOC (AIM).
* Jabber libraries.
* Prototypes of chat server and client frameworks built on top of
  the protocols.

%prep
%setup -qn TwistedWords-%{version}

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir}

%files
%defattr(0644,root,root,0755)
%doc LICENSE NEWS README doc/*
%dir %{py_platsitedir}/twisted/words/
%{py_platsitedir}/twisted/words/*
%{py_platsitedir}/twisted/plugins/*
%{py_platsitedir}/*.egg-info




