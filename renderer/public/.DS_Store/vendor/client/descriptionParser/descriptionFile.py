import logging
from pprint import pprint

from descriptionParser.description import Description

logger = logging.getLogger(__name__)


class DescriptionFile:
    def __init__(self, filePath, encoding="utf-16", lang="English"):
        self.filePath = filePath
        self.encoding = encoding
        self.lang = lang

        logger.debug(
            f"Initializing DescriptionFile with path: {filePath}, encoding: {encoding}, lang: {lang}"
        )

        fileLines = self.load(self.filePath)
        blocks = self.split_into_description_blocks(fileLines)

        self.descriptions = [Description(block, lang=self.lang) for block in blocks]
        self.descriptions_lookup = {d.id: d for d in self.descriptions}

        logger.debug(f"Loaded {len(self.descriptions)} descriptions.")

    def __str__(self):
        return f"DescriptionFile(descriptions={self.descriptions})"

    def load(self, filePath: str) -> list[str]:
        logger.debug(f"Loading file: {filePath} with encoding: {self.encoding}")

        with open(filePath, "r", encoding=self.encoding) as f:
            lines = f.readlines()

        logger.debug(f"Loaded {len(lines)} lines from the file.")

        # trim up until the first description block
        while not lines[0].startswith("description"):
            logger.debug("Removing line as it does not start with 'description'.")
            lines.pop(0)

        return lines

    def split_into_description_blocks(self, lines: list[str]) -> list[list[str]]:
        logger.debug("Splitting lines into description blocks.")

        blocks = [[]]

        for i in range(len(lines)):
            if lines[i].startswith("description"):
                if len(blocks) > 0 and len(blocks[-1]) > 0 and blocks[-1][-1] == "\n":
                    # remove last empty line
                    blocks[-1].pop()
                    logger.debug(
                        f"Removed last empty line from block {len(blocks) - 1}."
                    )
                blocks.append([])

            blocks[-1].append(lines[i])

        if len(blocks[-1]) > 0 and blocks[-1][-1] == "\n":
            # remove last empty line
            blocks[-1].pop()
            logger.debug(f"Removed last empty line from the final block.")

        if len(blocks[0]) == 0:
            blocks.pop(0)

        logger.debug(f"Created {len(blocks)} blocks of descriptions.")
        return blocks
