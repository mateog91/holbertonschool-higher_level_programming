#!/bin/bash
curl -i 0.0.0.0:5000 | cat | grep Content-Length: | cut -d ":" -f 2-
