# $Revision: 1.3 $
Summary:	Fonts for figlet - awesome ASCII-art banners generator
Summary(pl):	Czcionki dla figleta - programu do generowania napisów ASCII
Name:		figlet-fonts
# Version is last update date: yyyymmdd
Version:	20020602
Release:	1
License:	Free
Group:		Applications/Games
Source0:	ftp://ftp.plig.org/pub/figlet/fonts/contributed.tar.gz
URL:		http://st-www.cs.uiuc.edu/~chai/figlet.html
Buildarch:	noarch
Requires:	figlet
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pakiet zawiera dodatkowe czcionki dla programu figlet.

%description -l pl
This package contains extra fonts for figlet.

%prep
%setup -q -n contributed

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/figlet

rm -f banner.flf 
install *.{flf,flc} bdffonts/*.flf $RPM_BUILD_ROOT%{_datadir}/games/figlet

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc bdffonts/{README,bdffont1.txt} eftichessChart {eftiwall-chart,eftiwall}.txt
%{_datadir}/games/figlet
