Summary:	Tool for analysis of TCP dump files
Summary(pl.UTF-8):	Narzędzie do analizy zrzutów pakietów TCP
Summary(pt_BR.UTF-8):	Ferramenta para análise de arquivos de captura de tráfego de rede
Name:		tcptrace
Version:	6.6.7
Release:	2
Epoch:		1
License:	BSD
Group:		Applications/Networking
Source0:	http://www.tcptrace.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	68128dc1817b866475e2f048e158f5b9
Patch0:		ac264.patch
Patch1:		http://ftp.debian.org/debian/pool/main/t/tcptrace/%{name}_6.6.7-4.1.diff.gz
# Patch1-md5:	d073fb808e942f75399d035ba80c78cf
URL:		http://www.tcptrace.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex >= 2.5.31-4
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

%description -l pl.UTF-8
tcptrace to narzędzie do analizowania zrzutów pakietów TCP. tcptrace
jako dane wejściowe przyjmuje zrzuty stworzone przez popularne
programy typu tcpdump, snoop, etherpeek, HP Net Metrix, and WinDump.
tcptrace może generować kilka różnego rodzaju raportów na temat
połączeń, czasu ich trwania, bajtów, retransmisji, czasów round trip,
ogłoszeń okien itd. Może także generować statystyki graficzne do
przyszłej analizy.

%description -l pt_BR.UTF-8
tcptrace é uma ferramenta para análise de arquivos de captura de
tráfego de rede. Podem ser usados como arquivos de entrada os dados
produzidos por diversos sniffers populares, como tcpdump, snoop,
etherpeek, HP Net Metrix e WinDump. A saída gerada consiste em
informações de cada conexão vista, como tempo decorrido, bytes e
segmentos enviados e recebidos, retransmissões, tempos de resposta,
anúncios de janela, taxas, etc. Esta ferramenta também pode produzir
gráficos destes dados.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p tcptrace xpl2gpl	$RPM_BUILD_ROOT%{_bindir}
cp -a tcptrace.man $RPM_BUILD_ROOT%{_mandir}/man1/tcptrace.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc THANKS CHANGES FAQ README* ARGS
%attr(755,root,root) %{_bindir}/tcptrace
%attr(755,root,root) %{_bindir}/xpl2gpl
%{_mandir}/man1/tcptrace.1*
