Summary:	Fonts for figlet - awesome ASCII-art banners generator
Summary(pl):	Czcionki dla figleta - programu do generowania napisów ASCII
Name:		figlet-fonts
# Version is last update date: yyyymmdd
Version:	20050306
Release:	1
License:	Free
Group:		Applications/Games
Source0:	http://www.jave.de/figlet/figletfonts37.zip
# Source0-md5:	9acfdcb96c9a20abea9c6f706a591b91
URL:		http://www.jave.de/figlet/
BuildRequires:	unzip
Requires:	figlet
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains extra fonts for figlet.

%description -l pl
Pakiet zawiera dodatkowe czcionki dla programu figlet.

%prep
%setup -q -n fonts

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/figlet

rm -f {banner,big,block,bubble,digital,ivrit,lean,mini}.flf
rm -f {mnemonic,script,shadow,slant,small,smscript,smshadow}.flf
rm -f {smslant,standard,term}.flf
rm -f upper.flc
install *.{flf,flc} $RPM_BUILD_ROOT%{_datadir}/games/figlet

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {categoriestree,categories,files,fonts_readme}.txt
%{_datadir}/games/figlet/*
