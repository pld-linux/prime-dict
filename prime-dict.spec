Summary:	Dictionaries for PRIME - a Japanese PRedictive Input Method Editor
Summary(pl.UTF-8):	Słowniki dla PRIME'a - edytora przewidującej metody wprowadzania tekstu japońskiego
Name:		prime-dict
Version:	1.0.0
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://prime.sourceforge.jp/src/%{name}-%{version}.tar.gz
# Source0-md5:	41e36f11d927220917ba15bb8842a971
URL:		http://taiyaki.org/prime/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	prime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Dictionaries for PRIME - a Japanese PRedictive Input Method Editor.

%description -l pl.UTF-8
Słowniki dla PRIME'a (PRedictive Input Method Editor) - edytora
przewidującej metody wprowadzania tekstu japońskiego.

%prep
%setup -q

%build
%configure \
	--with-rubydir=%{ruby_rubylibdir}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%{ruby_rubylibdir}/prime/prime-dict-config.rb
%{_datadir}/prime/dict
