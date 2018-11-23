#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Modern-Perl
Version  : 1.20181021
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/Modern-Perl-1.20181021.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/Modern-Perl-1.20181021.tar.gz
Summary  : 'enable all of the features of Modern Perl with one import'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Modern-Perl-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Modern::Perl
------------
Modern Perl often relies on the presence of several core and CPAN pragmas and
modules.  Wouldn't it be nice to use them all with a single command?  Try this
one:

%package dev
Summary: dev components for the perl-Modern-Perl package.
Group: Development
Provides: perl-Modern-Perl-devel = %{version}-%{release}

%description dev
dev components for the perl-Modern-Perl package.


%package license
Summary: license components for the perl-Modern-Perl package.
Group: Default

%description license
license components for the perl-Modern-Perl package.


%prep
%setup -q -n Modern-Perl-1.20181021

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Modern-Perl
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Modern-Perl/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Modern/Perl.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Modern::Perl.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Modern-Perl/LICENSE
