#
# Conditional build:
%bcond_without	tests	# py.test based unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Namespace control and lazy-import mechanism
Summary(pl.UTF-8):	Kontrola przestrzeni nazw i mechanizm leniwego importu
Name:		python-apipkg
Version:	2.1.0
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/apipkg/
Source0:	https://files.pythonhosted.org/packages/source/a/apipkg/apipkg-%{version}.tar.gz
# Source0-md5:	831741a57e9fcb2b85c191a046916c8d
URL:		http://bitbucket.org/hpk42/apipkg
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
%{?with_tests:BuildRequires:	python-pytest}
BuildRequires:	python-setuptools >= 1:30.3.0
BuildRequires:	python-setuptools_scm
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
%{?with_tests:BuildRequires:	python3-pytest}
BuildRequires:	python3-setuptools >= 1:30.3.0
BuildRequires:	python3-setuptools_scm
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
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
Requires:	python3-modules >= 1:3.4

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

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python} -m pytest
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-apipkg-%{version}
cp -pr example/* $RPM_BUILD_ROOT%{_examplesdir}/python3-apipkg-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.rst
%{py_sitescriptdir}/apipkg
%{py_sitescriptdir}/apipkg-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%files -n python3-apipkg
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.rst
%{py3_sitescriptdir}/apipkg
%{py3_sitescriptdir}/apipkg-%{version}-py*.egg-info
%{_examplesdir}/python3-apipkg-%{version}
%endif
