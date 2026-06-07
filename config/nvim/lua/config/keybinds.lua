local keymap = vim.keymap
vim.g.mapleader = " "

keymap.set("n", "<leader>cd", vim.cmd.Ex)
keymap.set("n", "<C-d>", "<C-d>zz")
keymap.set("n", "<C-u>", "<C-u>zz")
keymap.set("n", "n", "nzzzv")
keymap.set("n", "N", "Nzzzv")

keymap.set("v", "J", ":m '>+1<CR>gv=gv")
keymap.set("v", "K", ":m '<-2<CR>gv=gv")

keymap.set("x", "<leader>p", [["_dP]])
keymap.set({"n", "v"}, "<leader>y", [["+y]])

keymap.set("n", "<leader>fi", function()
    require('telescope.builtin').find_files({ cwd = "~/.config/nvim" })
end)
