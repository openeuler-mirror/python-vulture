%global _empty_manifest_terminate_build 0
Name:		python-vulture
Version:	2.5
Release:	1
Summary:	Vulture finds unused code in Python programs. 
License:	MIT
URL:		https://github.com/jendrikseipp/vulture
Source0:	https://files.pythonhosted.org/packages/f2/7b/5f3249c9b3076bceb2839cf7ea9847e504d180e90dfac32300403a9e7139/vulture-2.5.tar.gz
BuildArch:	noarch

Requires:	python3-toml

%description
Vulture finds unused code in Python programs. This is useful for cleaning up and finding errors in large code bases. If you run Vulture on both your library and test suite you can find untested code.

%package -n python3-vulture
Summary:	Find dead code
Provides:	python-vulture
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-vulture
Vulture finds unused code in Python programs. This is useful for cleaning up and finding errors in large code bases. If you run Vulture on both your library and test suite you can find untested code.

%package help
Summary:	Development documents and examples for vulture
Provides:	python3-vulture-doc
%description help
Vulture finds unused code in Python programs. This is useful for cleaning up and finding errors in large code bases. If you run Vulture on both your library and test suite you can find untested code.

%prep
%autosetup -n vulture-2.5

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-vulture -f filelist.lst
%dir %{python3_sitelib}/vulture/__pycache__/

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Thu Jul 07 2022 hkgy <kaguyahatu@outlook.com> - 2.5-1
- Upgrade version to 2.5

* Tue Oct 12 2021 Python_Bot <Python_Bot@openeuler.org> - 2.3-1
- Package Init
