Summary:	Tool for analysis of TCP dump files
Summary(pl):	Narzêdzie do analizy zrzutów pakietów TCP
Summary(pt_BR):	Ferramenta para análise de arquivos de captura de tráfego de rede
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
tcptrace to narzêdzie do analizowania zrzutów pakietów TCP. tcptrace
jako dane wej¶ciowe przyjmuje zrzuty stworzone przez popularne
programy typu tcpdump, snoop, etherpeek, HP Net Metrix, and WinDump.
tcptrace mo¿e generowaæ kilka ró¿nego rodzaju raportów na temat
po³±czeñ, czasu ich trwania, bajtów, retransmisji, czasów round trip,
og³oszeñ okien itd. Mo¿e tak¿e generowaæ statystyki graficzne do
przysz³ej analizy.

%description -l pt_BR
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
