%define name	wmtv
%define version	0.6.5
%define release %mkrel 13
 
Name: 		%{name}
Version: 	%{version}
Release:	%{release} 
Source:		%{name}-%{version}.tar.bz2
Source1:	wmtvrc.europe
Source2:	wmtv-master.xpm
License: 	GPLv2+
Group:		Video
Summary:	WindowMaker dock.app that controls TV 
URL:		http://www.student.uwa.edu.au/~wliang
BuildRequires:	pciutils-devel xpm-devel
BuildRequires:	X11-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
wmtv is a WindowMaker dock.app that controls TV Cards which are
supported under the Linux Kernel 2.2.x series (mainly for cards based
on BrookTree BT848/848a/84 9a/878/879 chipsets: There are lots of cards
out there which uses these chipsets such as the Hauppauge WinTV,
Aimslab VideoExtreme, miroVIDEO PCTV, AverMedia TV Phone, etc).

%prep
%setup -n %{name}-%{version}

%build
%make

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/share/pixmaps
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
cp ${RPM_BUILD_DIR}/%{name}-%{version}/%{name} ${RPM_BUILD_ROOT}/%{_bindir}/%{name}
install -m644 %{SOURCE1} ${RPM_BUILD_ROOT}/%{_sysconfdir}/wmtvrc
install -m644 %{SOURCE2} ${RPM_BUILD_ROOT}%{_prefix}/share/pixmaps/%{name}.xpm

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=WMtv
Comment=WM Dock TV
TryExec=%{name}
Exec=%{name}
Icon=video_section
Terminal=false
StartupNotify=true
Categories=GNOME;GTK;AudioVideo;Audio;Video;Player;
Type=Application
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README wmtvrc.sample CREDITS COPYING CHANGES 
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/wmtvrc
%{_prefix}/share/pixmaps/%{name}.xpm
%{_datadir}/applications/mandriva-%{name}.desktop
