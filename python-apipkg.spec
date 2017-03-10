#
# Conditional build:
%bcond_without	tests	# py.test based unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Namespace control and lazy-import mechanism
Summary(pl.UTF-8):	Kontrola przestrzeni nazw i mechanizm leniwego importu
Name:		python-apipkg
Version:	1.4
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/apipkg
Source0:	https://pypi.python.org/packages/source/a/apipkg/apipkg-%{version}.tar.gz
# Source0-md5:	17e5668601a2322aff41548cb957e7c8
URL:		http://bitbucket.org/hpk42/apipkg
%if %{with python2}
BuildRequires:	python-modules >= 2.3
%{?with_tests:BuildRequires:	python-pytest}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
%{?with_tests:BuildRequires:	python3-pytest}
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With apipkg you can control the exported namespace of a Python package
and greatly reduce the number of imports for your users.

%description -l pl.UTF-8
Przy użyciu apipkg można kontrolować eksportowaną przestrzeń nazw
pakietu pythonowego i znacząco zredukować liczbę modułów importowaną
przez użytkowników.

%package -n python3-apipkg
Summary:	Namespace control and lazy-import mechanism
Summary(pl.UTF-8):	Kontrola przestrzeni nazw i mechanizm leniwego importu
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-apipkg
With apipkg you can control the exported namespace of a Python package
and greatly reduce the number of imports for your users.

%description -n python3-apipkg -l pl.UTF-8
Przy użyciu apipkg można kontrolować eksportowaną przestrzeń nazw
pakietu pythonowego i znacząco zredukować liczbę modułów importowaną
przez użytkowników.

%prep
%setup -q -n apipkg-%{version}

%build
%if %{with python2}
%py_build

%{?with_tests:%{__python} -mpytest}
%endif

%if %{with python3}
%py3_build

%{?with_tests:%{__python3} -mpytest}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.txt
%{py_sitescriptdir}/apipkg.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/apipkg-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-apipkg
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.txt
%{py3_sitescriptdir}/apipkg.py
%{py3_sitescriptdir}/__pycache__/apipkg.cpython-*.py[co]
%{py3_sitescriptdir}/apipkg-%{version}-py*.egg-info
%endif
