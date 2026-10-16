# Task runner — NOT a build. There is no compile step.
# Everything here is a convenience wrapper around scripts/ and shell.

SHELL := /usr/bin/env bash
.DEFAULT_GOAL := help

.PHONY: help verify lint guard icons package clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

verify: ## Verify manifest hashes match the tree
	bash scripts/verify-hashes.sh

lint: ## Lint markdown and shell
	@command -v shellcheck >/dev/null && shellcheck skills/*/scripts/*.sh scripts/*.sh || echo "shellcheck not installed, skipping"
	@command -v markdownlint >/dev/null && markdownlint '**/*.md' || echo "markdownlint not installed, skipping"

guard: ## Run the fleet's safety checks
	bash skills/muse-cname-guard/scripts/check-cname.sh
	bash skills/muse-cloudflare-deploy/scripts/check-secrets.sh

icons: ## Validate icon assets
	bash scripts/validate_icons.sh

package: ## Zip the whole project
	cd .. && zip -r fed-os-muse-skills.zip fed-os-muse-skills -x '*/node_modules/*' -x '*/.git/*'

clean: ## Remove generated artifacts
	rm -rf dist build *.zip
