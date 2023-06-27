PVMEISCSI Storage Backend for Cinder
-------------------------------

Overview
========

This charm provides a PVMEISCSI storage backend for use with the Cinder
charm.

To use:

    juju deploy cinder
    juju deploy cinder-pvmeiscsi
    juju add-relation cinder-pvmeiscsi cinder

Configuration
=============

See config.yaml for details of configuration options.
