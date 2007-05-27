#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	OptList
Summary:	Data::OptList - parse and validate simple name/value option pairs
#Summary(pl):	
Name:		perl-Data-OptList
Version:	0.101
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6e9bb994a8716112a78c1306261f4164
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Params::Util) >= 0.14
BuildRequires:	perl(Sub::Install) >= 0.92
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hashes are great for storing named data, but if you want more than one entry
for a name, you have to use a list of pairs.  Even then, this is really boring
to write:

  @values = (
    foo => undef,
    bar => undef,
    baz => undef,
    xyz => { ... },
  );

Just look at all those undefs!  Don't worry, we can get rid of those:

  @values = (
    map { $_ => undef } qw(foo bar baz),
    xyz => { ... },
  );

Aaaauuugh!  We've saved a little typing, but now it requires thought to read,
and thinking is even worse than typing.



# %description -l pl
# TODO

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
#%%{perl_vendorlib}/Data/OptList
%{_mandir}/man3/*
