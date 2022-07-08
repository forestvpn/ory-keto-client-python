VERSION ?= "v0.8.0-alpha.2"

validate:
	openapi-generator validate -i spec/$(VERSION).json

all: validate
	openapi-generator generate -g python -i spec/$(VERSION).json -o . \
		--git-host="github.com" \
		--git-user-id="forestvpn" --git-repo-id="ory-keto-client-python" \
		--additional-properties=projectName="forestvpn-ory-keto-client" \
		--additional-properties=packageName="ory_keto_client" \
		--additional-properties=packageUrl="https://github.com/forestvpn/ory-keto-client-python" \
		--additional-properties=packageVersion=$(VERSION) \
		--library=urllib3

