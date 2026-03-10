Summary:	zsh-lovers is a small project which tries to collect tips, tricks and examples for the Z shell
Summary(hu.UTF-8):	zsh-lovers egy kis project, amely megpróbálja összegyűjteni a tippeket, trükköket és példákat a Z shell-hez
Name:		zsh-lovers
Version:	0.11.0
Release:	1
License:	GPL v2
Group:		Documentation
Source0:	https://deb.grml.org/pool/main/z/zsh-lovers/%{name}_%{version}.tar.xz
# Source0-md5:	c221a4ad3b27995756c06345af15c8fe
URL:		https://grml.org/zsh/
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zsh-lovers is a small project which tries to collect tips, tricks and
examples for the Z shell.

%description  -l hu.UTF-8
zsh-lovers egy kis project, amely megpróbálja összegyűjteni a
tippeket, trükköket és példákat a Z shell-hez.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_mandir}/man1

cp -rf README.md zsh-lovers.1.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install zsh-lovers.1.txt $RPM_BUILD_ROOT%{_mandir}/man1/zsh-lovers.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%{_mandir}/man1/zsh-lovers.1*
