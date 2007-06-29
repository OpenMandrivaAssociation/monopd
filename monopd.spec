%define	version	0.9.1
%define release	1mdk

Summary:	Server for Monopoly-like board games
Name:		monopd
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Boards
URL:		http://www.unixcode.org/monopd/
Source:		http://www.unixcode.org/download/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{SOURCE0}.sig
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libmath++-devel >= 0.0.3
BuildRequires:	libcapsinetwork-devel >= 0.2.5

%description
Monopd is a dedicated game server daemon for playing Monopoly-like board
games. Clients such as Atlantik (KDE) and gtkAtlantic (GTK+) connect to
the server and communicate using short commands and XML messages.

Currently supported board games are Monopoly and Atlantic, a variation
on Monopoly-like games.

%prep
%setup -q

%build
%serverbuild
%configure2_5x \
	--bindir=%{_gamesbindir} \
	--datadir=%{_gamesdatadir} \
	--sysconfdir=%{_sysconfdir}/%{name}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

mv %{buildroot}%{_sysconfdir}/%{name}/monopd.conf-dist \
	%{buildroot}%{_sysconfdir}/%{name}/monopd.conf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc API AUTHORS ChangeLog COPYING NEWS README*
%config(noreplace) %{_sysconfdir}/%{name}
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
