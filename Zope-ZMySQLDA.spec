
%define prod_name ZMySQLDA

Summary:	Zope MySQL database adapter
Summary(pl):	Interfejs bazy danych MySQL do Zope
Name:		Zope-%{prod_name}
Version:	2.0.8
Release:	1
License:	ZPL
Source0:	http://www.zope.org/Members/adustman/Products/ZMySQLDA/%{prod_name}-%{version}.tar.gz
# Source0-md5:	74332272e53b13c6b19d3185d575699c
URL:		http://www.zope.org/Members/adustman/Products/ZMySQLDA/
Group:		Development/Languages/Python
Requires:	Zope
Requires:	python-MySQLdb
BuildRequires:	python-MySQLdb
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"

%define zope_dir	   %{_libdir}/zope
%define zope_productsdir   %{zope_dir}/Products

%description
Zope MySQL database adapter.

%description -l pl
Interfejs bazy danych MySQL do Zope.

%prep
%setup -q -c
mv -f lib/python/Products/%{prod_name}/* .
rm -rf lib

%build
%{python_compile}
%{python_compile_opt}

find . -name \*.py | xargs -r rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{zope_productsdir}/%{prod_name}

cp -a . $RPM_BUILD_ROOT%{zope_productsdir}/%{prod_name}
rm -f $RPM_BUILD_ROOT%{zope_productsdir}/%{prod_name}/*.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{zope_productsdir}/%{prod_name}
