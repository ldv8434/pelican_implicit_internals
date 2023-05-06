from pelican import signals
import re

def content_getter(generators):
#def content_getter(content):

	# compile regex for html
	# group 1 is link text, group 2 is link
	pattern = re.compile("href=\"([-\\\_\/.A-Za-z0-9]+\.(?:md|mkd|rst))\"")

#	local_link_replacer(content, pattern)
#	return;


	# Generators are hard-coded in the order of articles first, pages second
	# because that seems to be how pelican orders them
	# and I don't see enough of a reason to get them dynamically
	for c in generators[0].articles:
		local_link_replacer(c, pattern)
	for c in generators[0].translations:
		local_link_replacer(c, pattern)
	for c in generators[0].drafts:
		local_link_replacer(c, pattern)
	for c in generators[0].drafts_translations:
		local_link_replacer(c, pattern)

	for c in generators[1].pages:
		local_link_replacer(c, pattern)
	for c in generators[1].translations:
		local_link_replacer(c, pattern)
	for c in generators[1].hidden_pages:
		local_link_replacer(c, pattern)
	for c in generators[1].hidden_translations:
		local_link_replacer(c, pattern)
	for c in generators[1].draft_pages:
		local_link_replacer(c, pattern)
	for c in generators[1].draft_translations:
		local_link_replacer(c, pattern)

#	for p in generators:
#		if hasattr(p, '_update_content'):
#			p._update_content()
#		if hasattr(p, 'refresh_metadata_intersite_links'):
#			p.refresh_metadata_intersite_links()

def local_link_replacer(content, pattern):
	if content != None:
		# replace rst format
		content._content = pattern.sub(r'href="{filename}\1"', content._content)

#		print(content._content)
#		content._update_content(content._content,content.get_siteurl())

# register for pelican signals
def register():
	# register local_link_replacer to run at end of content object's init
	signals.all_generators_finalized.connect(content_getter)
	# register local_link_replacer to run at end of content object's init
#	signals.page_generator_preread.connect(content_getter)
