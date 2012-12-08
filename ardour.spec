Summary:	Digital Audio Workstatiton
Name:		ardour
Version:	2.8.16
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	5bafe41df00d25e7a357baaa1038f16d
BuildRequires:	aubio-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	gtkmm-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libgnomecanvasmm-devel
BuildRequires:	liblilv-devel
BuildRequires:	liblrdf-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	scons
BuildRequires:	soundtouch-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-DBOOST_SYSTEM_NO_DEPRECATED

%description
Digital Audio Workstation.

%prep
%setup -q

%build
%{__scons} \
	ARCH="%{rpmcflags}"	\
	DIST_LIBDIR=%{_lib}	\
	FREEDESKTOP=0		\
	FREESOUND=1		\
	LINKFLAGS=%{rpmldflags}	\
	PREFIX=%{_prefix}	\
	SYSLIBS=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__scons} \
	DESTDIR=$RPM_BUILD_ROOT	\
	install

cat > $RPM_BUILD_ROOT%{_desktopdir}/ardour.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=ardour2
Icon=ardour2
Terminal=false
Name=Ardour
Comment=Digital Audio Workstation
Categories=GTK;Audio;AudioVideo;Sequencer;
EOF

install icons/icon/ardour_icon_tango_48px_blue.png $RPM_BUILD_ROOT%{_pixmapsdir}/ardour2.png

mv $RPM_BUILD_ROOT%{_datadir}/locale/{pt,pt_BR}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{pt_PT,pt}

%find_lang gtk2_ardour
%find_lang libardour2
%find_lang libgtkmm2ext

cat {gtk2_ardour,libardour2,libgtkmm2ext}.lang > %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files
# -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/ardour2
%dir %{_libdir}/ardour2/engines
%dir %{_libdir}/ardour2/surfaces
%dir %{_libdir}/ardour2/vamp
%attr(755,root,root) %{_bindir}/ardour2
%attr(755,root,root) %{_libdir}/ardour2/ardour-%{version}
%attr(755,root,root) %{_libdir}/ardour2/engines/libclearlooks.so
%attr(755,root,root) %{_libdir}/ardour2/libardour.so
%attr(755,root,root) %{_libdir}/ardour2/libardour_cp.so
%attr(755,root,root) %{_libdir}/ardour2/libgtkmm2ext.so
%attr(755,root,root) %{_libdir}/ardour2/libmidi++.so
%attr(755,root,root) %{_libdir}/ardour2/libpbd.so
%attr(755,root,root) %{_libdir}/ardour2/librubberband.so
%attr(755,root,root) %{_libdir}/ardour2/libvamphostsdk.so
%attr(755,root,root) %{_libdir}/ardour2/libvampsdk.so
%attr(755,root,root) %{_libdir}/ardour2/surfaces/libardour_genericmidi.so
%attr(755,root,root) %{_libdir}/ardour2/surfaces/libardour_mackie.so
%attr(755,root,root) %{_libdir}/ardour2/surfaces/libardour_powermate.so
%attr(755,root,root) %{_libdir}/ardour2/surfaces/libardour_tranzport.so
%attr(755,root,root) %{_libdir}/ardour2/vamp/libardourvampplugins.so

%{_datadir}/ardour2
%{_sysconfdir}/ardour2

%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

