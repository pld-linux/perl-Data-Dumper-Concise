#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Dumper-Concise
Summary:	Data::Dumper::Concise - Less indentation and newlines plus sub deparsing
#Summary(pl.UTF-8):
Name:		perl-Data-Dumper-Concise
Version:	1.001
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSTROUT/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c11365c6a9e9eba8c869e043d4697eab
URL:		http://search.cpan.org/dist/Data-Dumper-Concise/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module always exports a single function, Dumper, which can be
called with a single reference value to dump that value or with no
arguments to return the Data::Dumper object it's created.

It exists, fundamentally, as a convenient way to reproduce a set of
Dumper options that we've found ourselves using across large numbers
of applications, primarily for debugging output.

The principle guiding theme is "all the concision you can get while
still having a useful dump and not doing anything cleverer than
setting Data::Dumper options" - it's been pointed out to us that
Data::Dump::Streamer can produce shorter output with less lines of
code. We know. This is simpler and we've never seen it segfault. But
for complex/weird structures, it generally rocks. You should use it as
well, when Concise is underkill. We do.

Why is deparsing on when the aim is concision? Because you often want
to know what subroutine refs you have when debugging and because if
you were planning to eval this back in you probably wanted to remove
subrefs first and add them back in a custom way anyway. Note that this
-does- force using the pure perl Dumper rather than the XS one, but
I've never in my life seen Data::Dumper show up in a profile so "who
cares?".

# %description -l pl.UTF-8
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

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Data/Dumper
%{perl_vendorlib}/Data/Dumper/*.pm
%{_mandir}/man3/*
