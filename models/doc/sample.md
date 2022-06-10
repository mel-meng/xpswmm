**Styling text**

You can indicate emphasis with bold, italic, strikethrough, subscript,
or superscript text in comment fields and .md files.

| Style                  | Syntax                 | Keyboard shortcut                         | Example                                      | Output                                 |
|------------------------|------------------------|-------------------------------------------|----------------------------------------------|----------------------------------------|
| Bold                   | \*\* \*\* or \_\_ \_\_ | Command+B (Mac) or Ctrl+B (Windows/Linux) | \*\*This is bold text\*\*                    | **This is bold text**                  |
| Italic                 | \* \* or \_ \_         | Command+I (Mac) or Ctrl+I (Windows/Linux) | \*This text is italicized\*                  | *This text is italicized*              |
| Strikethrough          | \~\~ \~\~              |                                           | \~\~This was mistaken text\~\~               |                                        |
| Bold and nested italic | \*\* \*\* and \_ \_    |                                           | \*\*This text is \_extremely\_ important\*\* | **This text is *extremely* important** |
| All bold and italic    | \*\*\* \*\*\*          |                                           | \*\*\*All this text is important\*\*\*       | ***All this text is important***       |
| Subscript              | \<sub\> \</sub\>       |                                           | \<sub\>This is a subscript text\</sub\>      | <sub>This is a subscript text</sub>    |
| Superscript            | \<sup\> \</sup\>       |                                           | \<sup\>This is a superscript text\</sup\>    | <sup>This is a superscript text</sup>  |

**Quoting text**

You can quote text with a \>.

Text that is not a quote

\> Text that is a quote

<img src="media/image1.png" style="width:6.5in;height:1.92083in"
alt="Rendered quoted text" />

**Tip:** When viewing a conversation, you can automatically quote text
in a comment by highlighting the text, then typing R. You can quote an
entire comment by clicking , then **Quote reply**. For more information
about keyboard shortcuts, see "[<u>Keyboard
shortcuts</u>](https://docs.github.com/en/articles/keyboard-shortcuts)."

**Quoting code**

You can call out code or a command within a sentence with single
backticks. The text within the backticks will not be formatted. You can
also press the Command+E (Mac) or Ctrl+E (Windows/Linux) keyboard
shortcut to insert the backticks for a code block within a line of
Markdown.

Use \`git status\` to list all new or modified files that haven't yet
been committed.

<img src="media/image2.png" style="width:6.08333in;height:0.41667in"
alt="Rendered inline code block" />

To format code or text into its own distinct block, use triple
backticks.

Some basic Git commands are:

\`\`\`

git status

git add

git commit

\`\`\`

<img src="media/image3.png" style="width:6.5in;height:1.26389in"
alt="Rendered code block" />

For more information, see "[<u>Creating and highlighting code
blocks</u>](https://docs.github.com/en/articles/creating-and-highlighting-code-blocks)."

If you are frequently editing code snippets and tables, you may benefit
from enabling a fixed-width font in all comment fields on GitHub. For
more information, see "[<u>Enabling fixed-width fonts in the
editor</u>](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/about-writing-and-formatting-on-github#enabling-fixed-width-fonts-in-the-editor)."

**Links**

You can create an inline link by wrapping link text in brackets \[ \],
and then wrapping the URL in parentheses ( ). You can also use the
keyboard shortcut Command+K to create a link. When you have text
selected, you can paste a URL from your clipboard to automatically
create a link from the selection.

You can also create a Markdown hyperlink by highlighting the text and
using the keyboard shortcut Command+V. If you'd like to replace the text
with the link, use the keyboard shortcut Command+Shift+V.

This site was built using \[GitHub Pages\](https://pages.github.com/).

<img src="media/image4.png" style="width:2.9375in;height:0.41667in"
alt="Rendered link" />

**Tip:** GitHub automatically creates links when valid URLs are written
in a comment. For more information, see "[<u>Autolinked references and
URLs</u>](https://docs.github.com/en/articles/autolinked-references-and-urls)."

**Section links**

You can link directly to a section in a rendered file by hovering over
the section heading to expose the link:

<img src="media/image5.png" style="width:6.5in;height:2.34375in"
alt="Section link within the README file for the github/scientist repository" />

**Relative links**

You can define relative links and image paths in your rendered files to
help readers navigate to other files in your repository.

A relative link is a link that is relative to the current file. For
example, if you have a README file in root of your repository, and you
have another file in *docs/CONTRIBUTING.md*, the relative link
to *CONTRIBUTING.md* in your README might look like this:

\[Contribution guidelines for this project\](docs/CONTRIBUTING.md)

GitHub will automatically transform your relative link or image path
based on whatever branch you're currently on, so that the link or path
always works. The path of the link will be relative to the current file.
Links starting with / will be relative to the repository root. You can
use all relative link operands, such as ./ and ../.

Relative links are easier for users who clone your repository. Absolute
links may not work in clones of your repository - we recommend using
relative links to refer to other files within your repository.

**Images**

You can display an image by adding ! and wrapping the alt text in \[ \].
Then wrap the link for the image in parentheses ().

!\[This is an
image\](https://myoctocat.com/assets/images/base-octocat.svg)

<img src="media/image6.png" style="width:6.5in;height:5.29097in"
alt="Rendered Image" />

GitHub supports embedding images into your issues, pull requests,
discussions, comments and .md files. You can display an image from your
repository, add a link to an online image, or upload an image. For more
information, see "[<u>Uploading
assets</u>](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#uploading-assets)."

**Tip:** When you want to display an image which is in your repository,
you should use relative links instead of absolute links.

Here are some examples for using relative links to display an image.

| Context                                                     | Relative Link                                                        |
|-------------------------------------------------------------|----------------------------------------------------------------------|
| In a .md file on the same branch                            | /assets/images/electrocat.png                                        |
| In a .md file on another branch                             | /../main/assets/images/electrocat.png                                |
| In issues, pull requests and comments of the repository     | ../blob/main/assets/images/electrocat.png?raw=true                   |
| In a .md file in another repository                         | /../../../../github/docs/blob/main/assets/images/electrocat.png      |
| In issues, pull requests and comments of another repository | ../../../github/docs/blob/main/assets/images/electrocat.png?raw=true |

**Note**: The last two relative links in the table above will work for
images in a private repository only if the viewer has at least read
access to the private repository which contains these images.

For more information, see "[<u>Relative
Links</u>](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#relative-links)."

**Specifying the theme an image is shown to**

You can specify the theme an image is displayed for in Markdown by using
the HTML \<picture\> element in combination with
the prefers-color-scheme media feature. We distinguish between light and
dark color modes, so there are two options available. You can use these
options to display images optimized for dark or light backgrounds. This
is particularly helpful for transparent PNG images.

For example, the following code displays a sun image for light themes
and a moon for dark themes:

\<picture\>

\<source media="(prefers-color-scheme: dark)"
srcset="https://user-images.githubusercontent.com/25423296/163456776-7f95b81a-f1ed-45f7-b7ab-8fa810d529fa.png"\>

\<source media="(prefers-color-scheme: light)"
srcset="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png"\>

\<img alt="Shows an illustrated sun in light color mode and a moon with
stars in dark color mode."
src="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png"\>

\</picture\>

The old method of specifying images based on the theme, by using a
fragment appended to the URL
(#gh-dark-mode-only or #gh-light-mode-only), is deprecated and will be
removed in favor of the new method described above.

**Lists**

You can make an unordered list by preceding one or more lines of text
with - or \*.

\- George Washington

\- John Adams

\- Thomas Jefferson

<img src="media/image7.png" style="width:1.95833in;height:0.91667in"
alt="Rendered unordered list" />

To order your list, precede each line with a number.

1\. James Madison

2\. James Monroe

3\. John Quincy Adams

<img src="media/image8.png" style="width:2.02083in;height:0.91667in"
alt="Rendered ordered list" />

**Nested Lists**

You can create a nested list by indenting one or more list items below
another item.

To create a nested list using the web editor on GitHub or a text editor
that uses a monospaced font, like [<u>Atom</u>](https://atom.io/), you
can align your list visually. Type space characters in front of your
nested list item, until the list marker character (- or \*) lies
directly below the first character of the text in the item above it.

1\. First list item

\- First nested list item

\- Second nested list item

**Note**: In the web-based editor, you can indent or dedent one or more
lines of text by first highlighting the desired lines and then
using Tab or Shift+Tab respectively.

<img src="media/image9.png" style="width:6.5in;height:0.725in"
alt="Nested list with alignment highlighted" />

<img src="media/image10.png" style="width:3.29167in;height:1.04167in"
alt="List with two levels of nested items" />

To create a nested list in the comment editor on GitHub, which doesn't
use a monospaced font, you can look at the list item immediately above
the nested list and count the number of characters that appear before
the content of the item. Then type that number of space characters in
front of the nested list item.

In this example, you could add a nested list item under the list
item 100. First list item by indenting the nested list item a minimum of
five spaces, since there are five characters (100. ) before First list
item.

100\. First list item

\- First nested list item

<img src="media/image11.png" style="width:2.46875in;height:0.76042in"
alt="List with a nested list item" />

You can create multiple levels of nested lists using the same method.
For example, because the first nested list item has seven characters
(␣␣␣␣␣-␣) before the nested list content First nested list item, you
would need to indent the second nested list item by seven spaces.

100\. First list item

\- First nested list item

\- Second nested list item

<img src="media/image12.png" style="width:3.03125in;height:0.90625in"
alt="List with two levels of nested items" />

For more examples, see the [<u>GitHub Flavored Markdown
Spec</u>](https://github.github.com/gfm/#example-265).

**Task lists**

To create a task list, preface list items with a hyphen and space
followed by \[ \]. To mark a task as complete, use \[x\].

\- \[x\] \#739

\- \[ \] https://github.com/octo-org/octo-repo/issues/740

\- \[ \] Add delight to the experience when all tasks are complete
:tada:

<img src="media/image13.png" style="width:6.5in;height:0.76458in"
alt="Rendered task list" />

If a task list item description begins with a parenthesis, you'll need
to escape it with \\:

\- \[ \] \\(Optional) Open a followup issue

For more information, see "[<u>About task
lists</u>](https://docs.github.com/en/articles/about-task-lists)."

**Mentioning people and teams**

You can mention a person
or [<u>team</u>](https://docs.github.com/en/articles/setting-up-teams) on
GitHub by typing @ plus their username or team name. This will trigger a
notification and bring their attention to the conversation. People will
also receive a notification if you edit a comment to mention their
username or team name. For more information about notifications, see
"[<u>About
notifications</u>](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications)."

**Note:** A person will only be notified about a mention if the person
has read access to the repository and, if the repository is owned by an
organization, the person is a member of the organization.

@github/support What do you think about these updates?

<img src="media/image14.png" style="width:4.5in;height:0.41667in"
alt="Rendered @mention" />

When you mention a parent team, members of its child teams also receive
notifications, simplifying communication with multiple groups of people.
For more information, see "[<u>About
teams</u>](https://docs.github.com/en/articles/about-teams)."

Typing an @ symbol will bring up a list of people or teams on a project.
The list filters as you type, so once you find the name of the person or
team you are looking for, you can use the arrow keys to select it and
press either tab or enter to complete the name. For teams, enter the
@organization/team-name and all members of that team will get subscribed
to the conversation.

The autocomplete results are restricted to repository collaborators and
any other participants on the thread.

**Referencing issues and pull requests**

You can bring up a list of suggested issues and pull requests within the
repository by typing #. Type the issue or pull request number or title
to filter the list, and then press either tab or enter to complete the
highlighted result.

For more information, see "[<u>Autolinked references and
URLs</u>](https://docs.github.com/en/articles/autolinked-references-and-urls)."

**Referencing external resources**

If custom autolink references are configured for a repository, then
references to external resources, like a JIRA issue or Zendesk ticket,
convert into shortened links. To know which autolinks are available in
your repository, contact someone with admin permissions to the
repository. For more information, see "[<u>Configuring autolinks to
reference external
resources</u>](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/configuring-autolinks-to-reference-external-resources)."

**Uploading assets**

You can upload assets like images by dragging and dropping, selecting
from a file browser, or pasting. You can upload assets to issues, pull
requests, comments, and .md files in your repository.

**Using emoji**

You can add emoji to your writing by typing :EMOJICODE:.

@octocat :+1: This PR looks great - it's ready to merge! :shipit:

<img src="media/image15.png" style="width:4.40625in;height:0.375in"
alt="Rendered emoji" />

Typing : will bring up a list of suggested emoji. The list will filter
as you type, so once you find the emoji you're looking for,
press **Tab** or **Enter** to complete the highlighted result.

For a full list of available emoji and codes, check out [<u>the
Emoji-Cheat-Sheet</u>](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md).

**Paragraphs**

You can create a new paragraph by leaving a blank line between lines of
text.

**Footnotes**

You can add footnotes to your content by using this bracket syntax:

Here is a simple footnote\[^1\].

A footnote can also have multiple lines\[^2\].

You can also use words, to fit your writing style more closely\[^note\].

\[^1\]: My reference.

\[^2\]: Every new line should be prefixed with 2 spaces.

This allows you to have a footnote with multiple lines.

\[^note\]:

Named footnotes will still render with numbers instead of the text but
allow easier identification and linking.

This footnote also has been made with a different syntax using 4 spaces
for new lines.

The footnote will render like this:

<img src="media/image16.png" style="width:6.26042in;height:2.6875in"
alt="Rendered footnote" />

**Note**: The position of a footnote in your Markdown does not influence
where the footnote will be rendered. You can write a footnote right
after your reference to the footnote, and the footnote will still render
at the bottom of the Markdown.

Footnotes are not supported in wikis.

**Hiding content with comments**

You can tell GitHub to hide content from the rendered Markdown by
placing the content in an HTML comment.

\<!-- This content will not appear in the rendered Markdown --\>

**Ignoring Markdown formatting**

You can tell GitHub to ignore (or escape) Markdown formatting by
using \\ before the Markdown character.

Let's rename \\\*our-new-project\\\* to \\\*our-old-project\\\*.

<img src="media/image17.png" style="width:3.875in;height:0.375in"
alt="Rendered escaped character" />

For more information, see Daring Fireball's "[<u>Markdown
Syntax</u>](https://daringfireball.net/projects/markdown/syntax#backslash)."

**Disabling Markdown rendering**

When viewing a Markdown file, you can click  at the top of the file to
disable Markdown rendering and view the file's source instead.

<img src="media/image18.png" style="width:6.5in;height:1.07917in"
alt="Display Markdown as source" />

Disabling Markdown rendering enables you to use source view features,
such as line linking, which is not possible when viewing rendered
Markdown files.