%global srcname     notifications
%global appname     io.elementary.notifications

%global commitdate  20201219

Name:           elementary-notifications
Version:        0
Release:        0.git%{commitdate}.1
Summary:        GTK Notifications Server
License:        GPLv3+

URL:            https://github.com/elementary/notifications
Source0:        https://github.com/elementary/notifications/archive/%{name}/%{srcname}-%{commitdate}.tar.gz

# Release is still missing, use git instead.

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libhandy-1)

%description
elementary Notifications is a GTK notification server for Pantheon.

%prep
%autosetup -n %{srcname}-%{commitdate}

%build
%meson
%meson_build


%install
%meson_install

%files
%license LICENSE
%doc README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}.desktop

%{_bindir}/%{appname}

%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml
