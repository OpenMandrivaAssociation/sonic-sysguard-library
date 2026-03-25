%define devname %mklibname SonicDELibksysguard -d
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.6
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

%define sonicsgrd_major 10
%define libsonicsgrd %mklibname SonicDESysGuardSystemStats
%define processcore_major 10
%define libprocesscore %mklibname sonicprocesscore
%define formatter_major 2
%define libformatter %mklibname SonicDESysGuardFormatter
%define sensorfaces_major 2
%define libsensorfaces %mklibname SonicDESysGuardSensorFaces
%define sensors_major 2
%define libsensors %mklibname SonicDESysGuardSensors
%define libsonicsignalplotter %mklibname sonicsignalplotter
%define liblsofui %mklibname lsofui
%define libprocessui %mklibname processui
%define desname %mklibname SonicDELibksysguard-designer -d

Name:		sonic-sysguard-library
Version:	6.6.3
Release:	%{?git:0.%{git}.}2
URL:            https://github.com/Sonic-DE/sonic-sysguard-library
# %if 0%{?git:1}
# Source0:	%url/archive/refs/tags/%version.tar.gz#/%name-%version.tar.gz
# %else
Source0: %url/archive/refs/tags/%version.tar.gz#/%name-%version.tar.gz
# %endif
Summary: SonicDE Frameworks 6 system monitoring framework

License: GPL
Group: System/Libraries
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6WebEngineCore)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(zlib)
BuildRequires: cmake(Qt6Designer)
BuildRequires: cmake(Qt6Sensors)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)

# pending rename
# BuildRequires: cmake(Plasma) >= 5.90.0
BuildRequires: %{_lib}SonicDE-devel

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6NewStuff)

# pending rename
# BuildRequires: cmake(KF6Auth)
BuildRequires: %{_lib}SonicFrameworksAuth-devel

BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Service)

# pending rename
#BuildRequires: cmake(KF6KIO)
BuildRequires: %{_lib}SonicFrameworksIO-devel

BuildRequires: cmake(KF6JobWidgets)
BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(libpcap)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libdrm)
BuildRequires: lm_sensors-devel
BuildRequires: gettext

BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

Requires: kf6-kquickcharts
Requires: %{libsonicsgrd} = %{EVRD}
Requires: %{libprocesscore} = %{EVRD}
Requires: %{libformatter} = %{EVRD}
Requires: %{libsensorfaces} = %{EVRD}
Requires: %{libsensors} = %{EVRD}

Conflicts: libksysguard

%description
SonicDE Frameworks 6 system monitoring framework.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/libksysguard.categories
%{_datadir}/dbus-1/interfaces/org.kde.ksystemstats1.xml
%{_libdir}/libexec/kf6/kauth/ksysguardprocesslist_helper
%dir %{_libdir}/libexec/ksysguard
%caps(cap_net_raw+ep) %{_libdir}/libexec/ksysguard/ksgrd_network_helper
%{_datadir}/dbus-1/system.d/org.kde.ksysguard.processlisthelper.conf
%{_datadir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
%{_qtdir}/qml/org/kde/ksysguard
%{_qtdir}/plugins/kf6/packagestructure/ksysguard_sensorface.so
%{_datadir}/knsrcfiles/systemmonitor-faces.knsrc
%{_datadir}/knsrcfiles/systemmonitor-presets.knsrc
%{_datadir}/ksysguard/sensorfaces
%{_datadir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy
%dir %{_qtdir}/plugins/ksysguard
%dir %{_qtdir}/plugins/ksysguard/process
%{_qtdir}/plugins/ksysguard/process/ksysguard_plugin_network.so
%{_qtdir}/plugins/ksysguard/process/ksysguard_plugin_gpu.so

#----------------------------------------------------------------------------

%package -n %{libsonicsgrd}
Summary: SonicDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}
Conflicts: %{_lib}KSysGuardSystemStats

%description -n %{libsonicsgrd}
%summary

%files -n %{libsonicsgrd}
%{_libdir}/libKSysGuardSystemStats.so.2
%{_libdir}/libKSysGuardSystemStats.so.6*

#----------------------------------------------------------------------------

%package -n %{libprocesscore}
Summary: SonicDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}
Conflicts: %{_lib}processcore

%description -n %{libprocesscore}
%summary

%files -n %{libprocesscore}
%{_libdir}/libprocesscore.so.%{processcore_major}
%{_libdir}/libprocesscore.so.6*

#----------------------------------------------------------------------------

%package -n %{libformatter}
Summary: SonicDE System Guard formatting library
Group: System/Libraries
Requires: %{name} = %{EVRD}
Conflicts:  %{_lib}KSysGuardFormatter

%description -n %{libformatter}
%summary

%files -n %{libformatter}
%{_libdir}/libKSysGuardFormatter.so.%{formatter_major}
%{_libdir}/libKSysGuardFormatter.so.6*

#----------------------------------------------------------------------------

%package -n %{libsensorfaces}
Summary: SonicDE System Guard sensor faces shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}
Conflicts: %{_lib}KSysGuardSensorFaces

%description -n %{libsensorfaces}
%summary

%files -n %{libsensorfaces}
%{_libdir}/libKSysGuardSensorFaces.so.%{sensorfaces_major}
%{_libdir}/libKSysGuardSensorFaces.so.6*

#----------------------------------------------------------------------------

%package -n %{libsensors}
Summary: SonicDE System Guard sensors shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}
Conflicts: %{_lib}KSysGuardSensors

%description -n %{libsensors}
%summary

%files -n %{libsensors}
%{_libdir}/libKSysGuardSensors.so.%{sensors_major}
%{_libdir}/libKSysGuardSensors.so.6*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary: Development files for the SonicDE system monitoring library
Group: Development/SonicDE and Qt
Requires: %{libsonicsgrd} = %{EVRD}
Requires: %{libprocesscore} = %{EVRD}
Requires: %{libformatter} = %{EVRD}
Requires: %{libsensorfaces} = %{EVRD}
Requires: %{libsensors} = %{EVRD}
Conflicts: %{_lib}KF6Libsysguard-devel
# Obsoletes: %{desname} < %{EVRD}

%description -n %{devname}
%summary

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KSysGuard
