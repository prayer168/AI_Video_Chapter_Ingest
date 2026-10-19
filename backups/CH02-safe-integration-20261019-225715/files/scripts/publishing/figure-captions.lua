-- Convert a canonical image + following bold caption paragraph into one
-- accessible Pandoc Figure node, keeping image, alt text, and caption together.
local function find_image(block)
  if block.t ~= "Figure" then return nil end
  for _, child in ipairs(block.content) do
    if child.t == "Plain" or child.t == "Para" then
      for _, inline in ipairs(child.content) do
        if inline.t == "Image" then return inline end
      end
    end
  end
  return nil
end

local display_numbers = {
  ["CH01-HOMAGE-FIG-001"] = "1-3A",
  ["CH01-HOMAGE-FIG-002"] = "1-4A",
  ["CH01-HOMAGE-FIG-003"] = "1-4B",
  ["CH01-HOMAGE-FIG-004"] = "1-4C",
  ["CH01-HOMAGE-FIG-005"] = "1-5A",
}

local function strip_display_prefix(inlines, display)
  if not inlines[1] or inlines[1].t ~= "Str" then return end
  local english = inlines[1].text == "Figure"
  local chinese = inlines[1].text == "圖"
  if not english and not chinese then return end
  inlines:remove(1)
  if inlines[1] and inlines[1].t == "Space" then inlines:remove(1) end
  if not inlines[1] or inlines[1].t ~= "Str" then return end
  local prefix = english and (display .. ".") or (display .. "｜")
  local current = inlines[1].text
  if current:sub(1, #prefix) == prefix then
    local updated = current:sub(#prefix + 1):gsub("^%s+", "")
    inlines[1].text = updated
    if updated == "" then
      inlines:remove(1)
      if inlines[1] and inlines[1].t == "Space" then inlines:remove(1) end
    end
  end
end

local function flatten_caption(inlines)
  local out = pandoc.List()
  for _, inline in ipairs(inlines) do
    if inline.t == "Strong" then
      for _, child in ipairs(inline.content) do out:insert(child) end
    else
      out:insert(inline)
    end
  end
  return out
end

function Pandoc(doc)
  if FORMAT:match("latex") and pandoc.utils.stringify(doc.meta.lang or ""):match("^zh") then
    local headers = doc.meta["header-includes"] or pandoc.MetaList{}
    headers:insert(pandoc.MetaBlocks{pandoc.RawBlock("latex", "\\captionsetup[figure]{name=圖}")})
    doc.meta["header-includes"] = headers
  end
  local output = pandoc.Blocks{}
  local i = 1
  while i <= #doc.blocks do
    local block = doc.blocks[i]
    local caption = doc.blocks[i + 1]
    local image = find_image(block)
    if image and caption and caption.t == "Para" and caption.content[1] and caption.content[1].t == "Strong" then
      local attrs = image.attr.attributes
      local alt = attrs["fig-alt"]
      if alt then
        image.attr.attributes["alt"] = alt
        image.attr.attributes["fig-alt"] = nil
      end
      local full_caption = flatten_caption(caption.content)
      local display = display_numbers[block.attr.identifier]
      if FORMAT:match("latex") and display then
        strip_display_prefix(full_caption, display)
        for _, child in ipairs(block.content) do
          if child.t == "Plain" or child.t == "Para" then
            child.content:insert(1, pandoc.RawInline("latex", "\\renewcommand{\\thefigure}{" .. display .. "}"))
            break
          end
        end
      end
      block.caption.long = pandoc.Blocks{pandoc.Plain(full_caption)}
      output:insert(block)
      i = i + 2
    else
      output:insert(block)
      i = i + 1
    end
  end
  doc.blocks = output
  return doc
end



