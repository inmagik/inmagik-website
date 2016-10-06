import re
from .models import NamedFile

CMS_FILE_REGEXP = r'([\[(]cmz-file://)(?P<name>.+)([\])])'
cms_file_regexp = re.compile(CMS_FILE_REGEXP)


def replace_cmz_files(content):
    def f(matchf):

        match = matchf.groups()
        name = match[1]
        try:
            instance = NamedFile.objects.get(name=name)
            out = match[0] + instance.upload.url + match[2]
            out = out.replace("cmz-file://", "")
            return out
        except:
            return match[0] + match[1] + match[2]

    processed_content = cms_file_regexp.sub(f, content)
    return processed_content
