#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	OptList
Summary:	Data::OptList - parse and validate simple name/value option pairs
Summary(pl.UTF-8):	Data::OptList - analiza i sprawdzanie poprawności prostych par opcji nazwa/wartość
Name:		perl-Data-OptList
Version:	0.104
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	95620446a0e49917b01a789e8a60cdd3
URL:		http://search.cpan.org/dist/Data-OptList/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Params-Util >= 0.14
BuildRequires:	perl-Sub-Install >= 0.92
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
%{perl_vendorlib}/Data/*.pm
%{_mandir}/man3/*
