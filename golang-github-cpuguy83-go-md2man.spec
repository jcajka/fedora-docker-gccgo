%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         cpuguy83
%global repo            go-md2man
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          2831f11f66ff4008f10e2cd7ed9a85e3d3fc2bed
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global gccgo_version  >= 5
%global golang_version >= 1.2.1-3

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1
Release:        4r%{?dist}
# Be ahead of Fedora
Epoch:          1
Summary:        Process markdown into manpages
License:        MIT
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Provides:       %{repo} = %{version}-%{release}

%description
%{repo} is a golang tool using blackfriday to process markdown into
manpages.

%package devel
%buildrequiresgo
BuildRequires:  golang(github.com/russross/blackfriday)
%requiresgo
BuildArch:      noarch
Summary:        A golang registry for global request variables
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/mangen) = %{version}-%{release}

%description devel
%{repo} is a golang tool using blackfriday to process markdown into
manpages.

This package contains library source intended for building other packages
which use %{project}/%{repo}.

%prep
%setup -qn %{repo}-%{commit}

%build
mkdir -p _build/src/%{provider}.%{provider_tld}/%{project}
ln -s $(pwd) ./_build/src/%{import_path}

BDIR=$(pwd)/_build

pushd $(pwd)/_build/src

%gobuild -p "$BDIR":%gopath %{import_path}

popd

%install
install -d -p %{buildroot}%{gopath}/src/%{import_path}/mangen
cp -pav *.go %{buildroot}%{gopath}/src/%{import_path}/
cp -pav mangen/*.go %{buildroot}%{gopath}/src/%{import_path}/mangen

# install go-md2man binary
install -d %{buildroot}%{_bindir}
install -p -m 755 ./_build/src/%{repo} %{buildroot}%{_bindir}

%check
#no test files so far

%files
%doc README.md
%{_bindir}/%{repo}

%files devel
%doc README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%dir %{gopath}/src/%{import_path}/*
%{gopath}/src/%{import_path}/*.go
%{gopath}/src/%{import_path}/*/*.go

%changelog
* Wed Feb 25 2015 jchaloup <jchaloup@redhat.com> - 1-4
- Bump to upstream 2831f11f66ff4008f10e2cd7ed9a85e3d3fc2bed
  related: #1156492

* Wed Feb 25 2015 jchaloup <jchaloup@redhat.com> - 1-3
- Add commit and shortcommit global variable
  related: #1156492

* Mon Oct 27 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1-2
- Resolves: rhbz#1156492 - initial fedora upload
- quiet setup
- no test files, disable check

* Thu Sep 11 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1-1
- Initial package
