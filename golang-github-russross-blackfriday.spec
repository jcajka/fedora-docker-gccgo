%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         russross
%global repo            blackfriday
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          77efab57b2f74dd3f9051c79752b2e8995c8b789
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global gopath /usr/share/gocode

Name:       golang-%{provider}-%{project}-%{repo}
Version:    1.2
Release:    5%{?dist}
Summary:    Markdown processor implemented in Go
License:    BSD
URL:        https://%{import_path}
Source0:    https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
BuildArch:  noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:  gcc-go
BuildRequires:  golang(github.com/shurcooL/sanitized_anchor_name)
Requires:   gcc-go
Requires:   golang(github.com/shurcooL/sanitized_anchor_name)
Summary:    Markdown processor implemented in Go
Provides:   golang(%{import_path}) = %{version}-%{release}
Provides:   golang(%{import_path}/mangen) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use %{project}/%{repo}.

%prep
%setup -qn %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}%{gopath}/src/%{import_path}/upskirtref
cp -pav *.go %{buildroot}%{gopath}/src/%{import_path}/
cp -pav upskirtref/* %{buildroot}%{gopath}/src/%{import_path}/upskirtref/

%check
GOPATH=%{gopath}:%{buildroot}%{gopath} go test -compiler gccgo -gccgoflags "$RPM_OPT_FLAGS" %{import_path}

%files devel
%doc README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%dir %{gopath}/src/%{import_path}/*
%{gopath}/src/%{import_path}/*.go
%{gopath}/src/%{import_path}/*/*

%changelog
* Mon Mar 02 2015 jchaloup <jchaloup@redhat.com> - 1.2-5
- Bump to upstream 77efab57b2f74dd3f9051c79752b2e8995c8b789
  Update spec file to used commit tarball
  related: #1156176

* Wed Feb 25 2015 jchaloup <jchaloup@redhat.com> - 1.2-4
- Add commit and shortcommit global variable
  related: #1156176

* Fri Oct 31 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.2-3
- include fedora/rhel arch conditionals

* Mon Oct 27 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.2-2
- runtime requires go.net/html

* Fri Oct 24 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.2-1
- Resolves: rhbz#1156176 - Initial package