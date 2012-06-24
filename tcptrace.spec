Summary:	Tool for analysis of TCP dump files
Summary(pl):	Narz�dzie do analizy zrzut�w pakiet�w TCP
Summary(pt_BR):	Ferramenta para an�lise de arquivos de captura de tr�fego de rede
Name:		tcptrace
Version:	6.4.2
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/Networking
Source0:	http://www.tcptrace.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	4ef34b76d6c060dc978ed3c777a15913
URL:		http://www.tcptrace.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex >= 2.5.31-4
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

%description -l pt_BR
tcptrace � uma ferramenta para an�lise de arquivos de captura de
tr�fego de rede. Podem ser usados como arquivos de entrada os dados
produzidos por diversos sniffers populares, como tcpdump, snoop,
etherpeek, HP Net Metrix e WinDump. A sa�da gerada consiste em
informa��es de cada conex�o vista, como tempo decorrido, bytes e
segmentos enviados e recebidos, retransmiss�es, tempos de resposta,
an�ncios de janela, taxas, etc. Esta ferramenta tamb�m pode produzir
gr�ficos destes dados.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install tcptrace xpl2gpl	$RPM_BUILD_ROOT%{_bindir}
install tcptrace.man		$RPM_BUILD_ROOT%{_mandir}/man1/tcptrace.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc THANKS CHANGES FAQ README* ARGS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
