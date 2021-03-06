#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-beautifulsoup4
Version  : 4.11.1
Release  : 90
URL      : https://files.pythonhosted.org/packages/e8/b0/cd2b968000577ec5ce6c741a54d846dfa402372369b8b6861720aa9ecea7/beautifulsoup4-4.11.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/e8/b0/cd2b968000577ec5ce6c741a54d846dfa402372369b8b6861720aa9ecea7/beautifulsoup4-4.11.1.tar.gz
Summary  : Screen-scraping library
Group    : Development/Tools
License  : MIT
Requires: pypi-beautifulsoup4-license = %{version}-%{release}
Requires: pypi-beautifulsoup4-python = %{version}-%{release}
Requires: pypi-beautifulsoup4-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(soupsieve)
BuildRequires : pypi-py
BuildRequires : pypi-pytest

%description
Beautiful Soup is a Python package for parsing HTML and XML documents.

%package license
Summary: license components for the pypi-beautifulsoup4 package.
Group: Default

%description license
license components for the pypi-beautifulsoup4 package.


%package python
Summary: python components for the pypi-beautifulsoup4 package.
Group: Default
Requires: pypi-beautifulsoup4-python3 = %{version}-%{release}

%description python
python components for the pypi-beautifulsoup4 package.


%package python3
Summary: python3 components for the pypi-beautifulsoup4 package.
Group: Default
Requires: python3-core
Provides: pypi(beautifulsoup4)
Requires: pypi(soupsieve)

%description python3
python3 components for the pypi-beautifulsoup4 package.


%prep
%setup -q -n beautifulsoup4-4.11.1
cd %{_builddir}/beautifulsoup4-4.11.1
pushd ..
cp -a beautifulsoup4-4.11.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656361126
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-beautifulsoup4
cp %{_builddir}/beautifulsoup4-4.11.1/COPYING.txt %{buildroot}/usr/share/package-licenses/pypi-beautifulsoup4/47fc2b45d986308bdbd2faa0457f696c581396db
cp %{_builddir}/beautifulsoup4-4.11.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-beautifulsoup4/47fc2b45d986308bdbd2faa0457f696c581396db
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-beautifulsoup4/47fc2b45d986308bdbd2faa0457f696c581396db

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
