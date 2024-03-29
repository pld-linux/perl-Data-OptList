#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	Data
%define	pnam	OptList
Summary:	Data::OptList - parse and validate simple name/value option pairs
Summary(pl.UTF-8):	Data::OptList - analiza i sprawdzanie poprawności prostych par opcji nazwa/wartość
Name:		perl-Data-OptList
Version:	0.114
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d63ec5d446eff1aaa5ba92bc13a52b77
URL:		https://metacpan.org/release/Data-OptList
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.78
BuildRequires:	perl-devel >= 1:5.12.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Params-Util >= 0.14
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Sub-Install >= 0.921
BuildRequires:	perl-Test-Simple >= 0.96
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::OptList simplifies storing name/value pairs.

%description -l pl.UTF-8
Data::OptList upraszcza zapisywanie par nazwa/wartość.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Data/OptList.pm
%{_mandir}/man3/Data::OptList.3pm*
