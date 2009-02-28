#
# $Id$
#
%define perlvendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define srcname project-builder

Summary:	Project Builder aka pb is a tool to produce packages for multiple distributions
Summary(fr):	Project Builder ou pb produit des paquets pour diverses distributions

Name:		project-builder
Version:	0.9.6
Release:	%mkrel 1
License:	GPL
Group:		System/Configuration/Packaging
Url:		http://trac.project-builder.org
Source:		ftp://ftp.project-builder.org/src/%{srcname}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)
BuildArch:	noarch
Requires:	perl >= 5.8.4, perl-DateManip, perl-ProjectBuilder, rpm-build,  

%description
Project Builder aka pb helps producing packages
for multiple distributions. It does that by minimizing
the duplication of information required and
a set a very simple configuration files.

%description -l fr
Project Builder ou pb est un programme pour produire des paquets pour 
diverses distributions.
Il réalise cela en minimisant la duplication des informations requises 
et par un jeu de fichiers de configuration très simples.

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor destdir=${RPM_BUILD_ROOT}/ 
make

%install
%{__rm} -rf %{buildroot}
make DESTDIR=${RPM_BUILD_ROOT} install
find ${RPM_BUILD_ROOT} -type f -name perllocal.pod -o -name .packlist -o -name '*.bs' -a -size 0 | xargs rm -f
find ${RPM_BUILD_ROOT} -type d -depth | xargs rmdir --ignore-fail-on-non-empty

%check
make test

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS AUTHORS
%doc INSTALL COPYING README

%{perlvendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
