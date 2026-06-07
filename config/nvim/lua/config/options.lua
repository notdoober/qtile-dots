vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.cursorline = true
vim.opt.shiftwidth = 4
vim.opt.tabstop = 4
vim.opt.expandtab = true
vim.opt.smartindent = true
vim.opt.termguicolors = true
vim.opt.clipboard = "unnamedplus"

local function apply_transparency()
    local hl_groups = {
        "Normal", "NormalFloat", "SignColumn", "LineNr", "FoldColumn",
        "Window", "StatusLine", "StatusLineNC", "VertSplit", "WinSeparator",
        "EndOfBuffer", "TabLine", "TabLineFill", "TabLineSel"
    }
    for _, group in ipairs(hl_groups) do
        vim.cmd(string.format("highlight %s guibg=NONE ctermbg=NONE", group))
    end
end

vim.api.nvim_create_autocmd("ColorScheme", {
    pattern = "*",
    callback = apply_transparency,
})
