
%define prod_name ZMySQLDA

Summary:	Zope MySQL database adapter. 
Name:		Zope-%{prod_name}
Version:	2.0.8
Release:	1
License:	ZPL
Source0:	http://www.zope.org/Members/adustman/Products/%{prod_name}/%{prod_name}-%{version}.tar.gz
URL:		http://www.zope.org/Members/adustman/Products/%{prod_name}
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
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

%prep
%setup -q -c -a 0 -n %{name}-%{version}
mv lib/python/Products/%{prod_name}/* .
rm -rf lib

%build
%{python_compile}
%{python_compile_opt}

find . -name \*.py | xargs -r rm -f
gzip -9nf *.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{zope_productsdir}/%{prod_name}

cp -a . $RPM_BUILD_ROOT%{zope_productsdir}/%{prod_name}
rm -f $RPM_BUILD_ROOT%{zope_productsdir}/%{prod_name}/*.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz 
%{zope_productsdir}/%{prod_name}
