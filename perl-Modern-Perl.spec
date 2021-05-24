#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Modern-Perl
Version  : 1.20200211
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/Modern-Perl-1.20200211.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/Modern-Perl-1.20200211.tar.gz
Summary  : 'enable all of the features of Modern Perl with one import'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Modern-Perl-license = %{version}-%{release}
Requires: perl-Modern-Perl-perl = %{version}-%{release}
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
Requires: perl-Modern-Perl = %{version}-%{release}

%description dev
dev components for the perl-Modern-Perl package.


%package license
Summary: license components for the perl-Modern-Perl package.
Group: Default

%description license
license components for the perl-Modern-Perl package.


%package perl
Summary: perl components for the perl-Modern-Perl package.
Group: Default
Requires: perl-Modern-Perl = %{version}-%{release}

%description perl
perl components for the perl-Modern-Perl package.


%prep
%setup -q -n Modern-Perl-1.20200211
cd %{_builddir}/Modern-Perl-1.20200211

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Modern-Perl
cp %{_builddir}/Modern-Perl-1.20200211/LICENSE %{buildroot}/usr/share/package-licenses/perl-Modern-Perl/e4b87ee67b79a6af319bd3182902d79c3d318714
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Modern::Perl.3
/usr/share/man/man3/odern::Perl.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Modern-Perl/e4b87ee67b79a6af319bd3182902d79c3d318714

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Modern/Perl.pm
/usr/lib/perl5/vendor_perl/5.34.0/odern/Perl.pm
