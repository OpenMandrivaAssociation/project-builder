#
# $Id$
#
%define perlvendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define srcname project-builder

Summary:	Project Builder helps providing multi-OSes Continuous Packaging
Summary(fr):	Project Builder ou pb produit des paquets pour diverses distributions

Name:		project-builder
Version:	0.12.5
Release:	1
License:	GPL
Group:		System/Configuration/Packaging
Url:		http://trac.project-builder.org
Source:		ftp://ftp.project-builder.org/src/%{srcname}-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl >= 5.8.4
Requires:	perl-DateManip
Requires:	perl-ProjectBuilder >= 0.10.1
Requires:	rpm-build
BuildRequires: perl-devel

%description
ProjectBuilder aka pb helps producing packages
for multiple OSes (Linux distributions, Solaris, ...).
It does that by minimizing
the duplication of information required and
a set a very simple configuration files.
It implements a Continuous Packaging approach.

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor destdir=%{buildroot}
make

%install
%makeinstall_std
find %{buildroot} -type f -name perllocal.pod -o -name .packlist -o -name '*.bs' -a -size 0 | xargs rm -f
find %{buildroot} -type d -depth | xargs rmdir --ignore-fail-on-non-empty

%check
make test

%files
%doc NEWS AUTHORS
%doc INSTALL COPYING README

%{perlvendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
