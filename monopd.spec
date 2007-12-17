%define	version	0.9.3
%define release	%mkrel 1

Summary:	Server for Monopoly-like board games
Name:		monopd
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Boards
URL:		http://www.unixcode.org/monopd/
Source:		http://www.unixcode.org/download/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{SOURCE0}.sig
Patch0:		monopd-0.9.3-dosfix.diff
BuildRequires:	libmath++-devel >= 0.0.3
BuildRequires:	libcapsinetwork-devel >= 0.3.0

%description
Monopd is a dedicated game server daemon for playing Monopoly-like board
games. Clients such as Atlantik (KDE) and gtkAtlantic (GTK+) connect to
the server and communicate using short commands and XML messages.

Currently supported board games are Monopoly and Atlantic, a variation
on Monopoly-like games.

%prep
%setup -q
%patch0 -p1

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
