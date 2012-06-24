Summary:	Tool for analysis of TCP dump files
Summary(pl):	Narz�dzie do analizy zrzut�w pakiet�w TCP
Name:		tcptrace
Version:	6.0.1
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/Networking
Source0:	http://www.tcptrace.org/download/%{name}.%{version}.tar.gz
URL:		http://www.tcptrace.org/
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tcptrace is a tool for analysis of TCP dump files. It can take as
input the files produced by several popular packet-capture programs,
including tcpdump, snoop, etherpeek, HP Net Metrix, and WinDump.
tcptrace can produce several different types of output containing
information on each connection seen, such as elapsed time, bytes and
segments sent and recieved, retransmissions, round trip times, window
advertisements, throughput, and more. It can also produce a number of
graphs for further analysis.

%description -l pl
tcptrace to narz�dzie do analizowania zrzut�w pakiet�w TCP. tcptrace
jako dane wej�ciowe przyjmuje zrzuty stworzone przez popularne
programy typu tcpdump, snoop, etherpeek, HP Net Metrix, and WinDump.
tcptrace mo�e generowa� kilka r�nego rodzaju raport�w na temat
po��cze�, czasu ich trwania, bajt�w, retransmisji, czas�w round trip,
og�osze� okien itd. Mo�e tak�e generowa� statystyki graficzne do
przysz�ej analizy.

%prep
%setup -q -n %{name}.%{version}

%build
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

install tcptrace	$RPM_BUILD_ROOT%{_sbindir}
install tcptrace.man	$RPM_BUILD_ROOT%{_mandir}/man1/tcptrace.1

gzip -9nf THANKS CHANGES FAQ README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*
